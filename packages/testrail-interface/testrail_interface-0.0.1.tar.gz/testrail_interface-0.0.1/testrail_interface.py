import sys
import os
import re
import argparse
from datetime import datetime, timedelta
from collections import ChainMap
import base64
import json
import requests

TR_DOMAIN = os.environ.get('TR_DOMAIN')
TR_USERNAME = os.environ.get('TR_USERNAME')
TR_API_KEY = os.environ.get('TR_API_KEY')
TR_PROJECT_ID = os.environ.get('TR_PROJECT_ID')

new_run_keys = ['suite_id', 'description', 'milestone_id',
                    'assignedto_id', 'include_all', 'refs']

manual_rest_pattern = r"\[[M|М|м|m]\]"

descriptions = {
    "flags": {
        '-l': 'Вывод подробного отчёта в консоль',
        '-f': 'Пути до файлов отчётов. Возможные варианты: -f path1 path2... или -f path1 -f path2',
        '-d': 'Пути до директорий с отчётами. Возможные варианты: -d path1 path2... или -d path1 -d path2'
    },
    "modules": {
        "get_run_id": 'Получение ID последнего активного тест-рана',
        "weekly_update": 'Проверка того, что последний тест-ран младше недели. Иначе создание нового рана',
        "manual_retest": 'Сброс статусов ручных тест-кейсов в секции',
        "send_report": 'Отправка отчётов из файлов (для последнего тест-рана)',
    },
    "params": {
        "request": 'Название команды (список см. ниже)',
        "section_name": 'Название секции с тестами',

    }
}

parser = argparse.ArgumentParser(description='Хендлер для работы с API TestRails')
parser.add_argument('-l', action='store_true',
                    help=descriptions['flags']['-l'])
parser.add_argument('request', metavar='module_name', type=str,
                    help=descriptions['params']['request'], nargs=1)

group1 = parser.add_argument_group('get_run_id', descriptions['modules']['get_run_id'])
group2 = parser.add_argument_group('weekly_update', descriptions['modules']['weekly_update'])
group3 = parser.add_argument_group('manual_retest', descriptions['modules']['manual_retest'])
group3.add_argument('section_name', type=str, nargs='*',
                    help=descriptions['params']['section_name'], default='')

group4 = parser.add_argument_group('send_report', 'send_report description')
group4.add_argument('-f', metavar='report_path', type=str,
                    help=descriptions['flags']['-f'], nargs='*', dest='paths')
group4.add_argument('-d', metavar='report_path', type=str,
                    help=descriptions['flags']['-d'], nargs='*', dest='dir')


class APIClient:
    def __init__(self, base_url):
        self.user = ''
        self.password = ''
        if not base_url.endswith('/'):
            base_url += '/'
        self.__url = base_url + 'index.php?/api/v2/'

    def send_get(self, uri, filepath=None):
        """Issue a GET request (read) against the API.

        Args:
            uri: The API method to call including parameters, e.g. get_case/1.
            filepath: The path and file name for attachment download; used only
                for 'get_attachment/:attachment_id'.

        Returns:
            A dict containing the result of the request.
        """
        return self.__send_request('GET', uri, filepath)

    def send_post(self, uri, data):
        """Issue a POST request (write) against the API.

        Args:
            uri: The API method to call, including parameters, e.g. add_case/1.
            data: The data to submit as part of the request as a dict; strings
                must be UTF-8 encoded. If adding an attachment, must be the
                path to the file.

        Returns:
            A dict containing the result of the request.
        """
        return self.__send_request('POST', uri, data)

    def __send_request(self, method, uri, data):
        url = self.__url + uri

        auth = str(
            base64.b64encode(
                bytes('%s:%s' % (self.user, self.password), 'utf-8')
            ),
            'ascii'
        ).strip()
        headers = {'Authorization': 'Basic ' + auth}

        if method == 'POST':
            if uri[:14] == 'add_attachment':    # add_attachment API method
                files = {'attachment': (open(data, 'rb'))}
                response = requests.post(url, headers=headers, files=files)
                files['attachment'].close()
            else:
                headers['Content-Type'] = 'application/json'
                payload = bytes(json.dumps(data), 'utf-8')
                response = requests.post(url, headers=headers, data=payload)
        else:
            headers['Content-Type'] = 'application/json'
            headers['x-api-ident'] = 'beta'
            response = requests.get(url, headers=headers)

        if response.status_code > 201:
            try:
                error = response.json()
            except:     # response.content not formatted as JSON
                error = str(response.content)
            raise APIError('TestRail API returned HTTP %s (%s)' % (response.status_code, error))
        else:
            if uri[:15] == 'get_attachment/':   # Expecting file, not JSON
                try:
                    open(data, 'wb').write(response.content)
                    return (data)
                except:
                    return ("Error saving attachment.")
            else:
                try:
                    return response.json()
                except: # Nothing to return
                    return {}


class APIError(Exception):
    pass


class TestRailsHandler:
    def __init__(self):
        self._username = TR_USERNAME
        self._password = TR_API_KEY
        self._url = 'https://' + TR_DOMAIN
        self._project_id = TR_PROJECT_ID
        self.create_client()

    def create_client(self):
        self.tr_client = APIClient(self._url)
        self.tr_client.user = self._username
        self.tr_client.password = self._password

    def get_update_weekly(self, params):
        latest_test_run = self.get_last_opened_run
        last_run_creation_date = datetime.fromtimestamp(latest_test_run['created_on'])
        if params['l']:
            print(f"Last run creation date is {last_run_creation_date}")
        if last_run_creation_date < datetime.now() - timedelta(days=7):
            print(f'Test run with ID {latest_test_run["id"]} is too old, recreating')

            new_run_data = {}
            new_run_data['name'] = f'Automated test run {datetime.now().date().strftime("%d-%m-%y")}'
            if params['l']:
                print(f"New run name is {new_run_data['name']}")
            for key in new_run_keys:
                new_run_data[key] = latest_test_run[key]

            self.close_run(latest_test_run['id'])
            latest_test_run = self.tr_client.send_post(f'add_run/{self._project_id}', new_run_data)
        return latest_test_run['id']

    def close_run(self, id):
        self.tr_client.send_post(f'close_run/{id}', {"run_id": id})

    @property
    def get_last_opened_run(self):
        return self.tr_client.send_get(f'get_runs/{self._project_id}&is_completed=0')['runs'][0]

    @staticmethod
    def get_all_child(sections, parent_id, parent_name):
        if any([i['parent_id'] == parent_id for i in sections]):
            for i in [s for s in sections if s['parent_id'] == parent_id]:
                yield from TestRailsHandler.get_all_child(sections, i['id'], i['name'])
        yield {parent_id: parent_name}

    def reset_manual_tests(self, params):

        """
        ПОлучаем по имени секции её ID
        Затем вытаскиваем все тесткейсы внутри этой секции. Если внутри секции есть секции с М,
        ставим все тесты в них в ретест; иначе ставим все тесты в секции в ретест. На выходе
        кидаем запрос. Фин
        :param section:
        :return:
        """
        assert len(params['section_name']), 'Отсутствует название группы и/или секции'
        section = params['section_name'][0]


        test_sections = self.tr_client.send_get(f'get_sections/{self._project_id}')['sections']
        test_cases = self.tr_client.send_get(f'get_cases/{self._project_id}')['cases']
        parent_sec_id = [sec['id'] for sec in test_sections if sec['name'] == section][0]
        run_id = self.get_last_opened_run['id']

        assert parent_sec_id, f"Отсутствует группа с таким названием {section}"

        print(f'Reseting manual tests in {section}')
        print(f'Last opened run: {run_id}')


        child_sections_in_parent = \
            dict(ChainMap(*list(self.get_all_child(test_sections, parent_sec_id, section))))
        manual_child_sections = \
            {id: name for id, name in child_sections_in_parent.items()
             if re.search(manual_rest_pattern, name)}
        manual_case_ids = [[case['id'], case['title'], case['section_id']] for case in test_cases
                           if case['section_id'] in manual_child_sections.keys()
                           or (
                                   re.search(manual_rest_pattern, case['title']) and
                                   case['section_id'] in child_sections_in_parent.keys()
                           )]
        if params['l']:
            print(f'Manual cases:')
            for case_id, case_title, parent_id in manual_case_ids:
                print(f"[{child_sections_in_parent[parent_id]}] ID {case_id} - {case_title}")

        post_request = \
            {"results": [{"case_id": case[0], "status_id": 4} for case in manual_case_ids]}
        self.tr_client.send_post(f'add_results_for_cases/{run_id}', post_request)
        return "Done"

    @staticmethod
    def add_results_for_cases(test: dict, body: dict) -> dict:
        case_id_found = False
        for marker in test['markers'].split(', '):
            if 'testrail_' in marker:
                        case_id = marker.split('_')[1]
                        # print(case_id)
                        case_id_found = True
        if test['result'] == 'PASSED':
            status_id = 1
        elif test['result'] == 'FAILED':
            status_id = 5
        else:
            status_id = 2
        if len(test['test_steps'])  == 1:
            payload = str(test['test_steps'][0]['expected']) + "\n"
        else:
            payload = ""
        if test['message'] != None:
            message = test['message']
        else:
            message = ""
        if case_id_found:
            result = {
                "case_id": case_id,
                "status_id": status_id,
                "comment": payload + message,
            }
            body['results'].append(result)
        return(body)

    def send_report(self, params):
        run_id = self.get_last_opened_run['id']

        assert params['paths'] or params['dir'], "Должны быть заданы путь к папке/пути к файлам"
        if params['paths']:
            paths = params['paths']
            reports = [os.path.abspath(i) for i in paths]
            master_path = reports[0]
            master_report = json.load(open(master_path))
            reports = reports[1:]
        elif params['dir']:
            dirname = params['dir'][0]
            reports = [os.path.join(os.getcwd(), dirname, i) for i in os.listdir(dirname)]
            master_path = reports[0]
            master_report = json.load(open(master_path))
            reports = reports[1:]

        print(f'Using {master_path} as base report') if params['l'] else None

        for report_path in reports:
            browser = re.search("output_(\w*).json", report_path).group(1)
            report = json.load(open(report_path))
            print(f'Processing {report_path}') if params['l'] else None
            assert len(report) == len(master_report), f'Разный состав отчётов {master_path} и {report_path}'
            for j in range(len(report)):
                if report[j]['class_name'] is None:
                    if report[j]['result'] == 'FAILED':
                        print(f'Found new failed test: {report[j]["test_name"]}') if params['l'] else None
                        master_report[j]['result'] = 'FAILED'
                        if master_report[j]['message'] is None:
                            master_report[j]['message'] = f'{browser} browser'
                        else:
                            master_report[j]['message'] = f'{browser} browser\n{master_report[j]["message"]}'

                # send every test in class
                else:
                    print(f'Found class of tests {report[j]["class_name"]}') if params['l'] else None
                    for k in range(len(report[j]['tests'])):
                        if report[j]['tests'][k]['result'] == 'FAILED':
                            master_report[j]['tests'][k]['result'] = 'FAILED'
                            if master_report[j]['tests'][k]['message'] is None:
                                master_report[j]['tests'][k]['message'] = f'{browser} browser'
                            else:
                                master_report[j]['message'] = f'{browser} browser\n{master_report[j]["message"]}'

        body = {"results": []}
        for j in range(len(master_report)):
            if master_report[j]['class_name'] is None:
                body = TestRailsHandler.add_results_for_cases(master_report[j], body)

            # send every test in class
            else:
                for k in range(len(master_report[j]['tests'])):
                    body = TestRailsHandler.add_results_for_cases(master_report[j]['tests'][k], body)

        self.tr_client.send_post(f'add_results_for_cases/{run_id}', body)

def main(args):

    params = vars(parser.parse_args(args[1:]))
    request = params['request'][0]

    tr_handler = TestRailsHandler()
    if request == 'weekly_update':
        return tr_handler.get_update_weekly(params)
    elif request == 'get_run_id':
        return tr_handler.get_last_opened_run['id']
    elif request == 'manual_retest':
        return tr_handler.reset_manual_tests(params)
    elif request == 'send_report':
        return tr_handler.send_report(params)
    else:
        raise TypeError(f"Неизвестный аргумент: {request}")


if __name__ == '__main__':
    print(main(sys.argv))