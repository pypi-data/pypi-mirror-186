import unittest
import os
import stretch_body.hello_utils as hu
import yaml
from colorama import Fore, Style

class TestBase():
    def __init__(self, test_name):
        print(Style.BRIGHT + '{}'.format(test_name))
        print('=' * len(test_name) + Style.RESET_ALL)

        self.timestamp = hu.create_time_string()
        self.test_name = test_name
        self.fleet_id = os.environ['HELLO_FLEET_ID']

        results_directory =os.environ['HELLO_FLEET_PATH']+'/log/diagnostic_check'#+self.timestamp

        os.system('mkdir -p %s' % results_directory)
        self.results_directory = results_directory
        self.results_directory_test_specific = self.results_directory + '/' + test_name
        self.hints=[]
        self.params_dict = {}
        self.data_dict = {}
        self.test_status = {}

        self.result_data_dict = {'params': None,
                                 'test_status': None,
                                 'data': None,
                                 'FAILS': None,
                                 'ERRORS': None}
        self.check_test_results_directories()

    def add_hint(self,hint):
        self.hints.append(hint)

    def check_test_results_directories(self):
        # self.update_production_repo()
        if not os.path.isdir(self.results_directory):
            os.system('mkdir -p {}'.format(self.results_directory))
        self.test_result_dir = '{}/{}'.format(self.results_directory, self.test_name)

        if not os.path.isdir(self.results_directory):
            os.system('mkdir -p {}'.format(self.test_result_dir))

        self.test_file_dir = '{}/{}'.format(self.results_directory, self.test_name)
        if not os.path.isdir(self.test_file_dir):
            os.system('mkdir -p {}'.format(self.test_file_dir))

    def save_test_result(self, test_status=None):
        """
        This function forces the practice of unit tests to produce result dict with the three fields
        """
        self.result_data_dict['test_status'] = test_status
        self.result_data_dict['params'] = self.params_dict
        self.result_data_dict['data'] = self.data_dict

        print(yaml.dump(self.result_data_dict['test_status']))
        self.check_test_results_directories()
        test_file_name = self.test_name + '_' + self.timestamp + '.yaml'
        filename = self.test_file_dir + '/' + test_file_name
        with open(filename, 'w') as file:
            documents = yaml.dump(self.result_data_dict, file)
        print('Test data saved to : {}'.format(filename))

    def log_params(self, key, value):
        self.params_dict[key] = value

    def log_data(self, key, value):
        self.data_dict[key] = value

    def log_fails(self, failures):
        self.result_data_dict['FAILS'] = self.parse_TestErrors(failures)

    def log_errors(self, errors):
        self.result_data_dict['ERRORS'] = self.parse_TestErrors(errors)

    def parse_TestErrors(self, failures):
        fails = []
        for f in failures:
            test_id = str(f[0].id())
            out = str(f[1])
            out_lines = out.split('\n')
            fails.append({test_id: out_lines})
        return fails

    def save_TestResult(self, result):
        ok = result.wasSuccessful()
        errors = result.errors
        failures = result.failures
        if ok:
            print(Fore.GREEN)
            print('All Test Cases passed')
            self.save_test_result(test_status={'status': 'SUCCESS',
                                               'errors': len(errors),
                                               'failures': len(failures),
                                               'hints': None})
            print(Style.RESET_ALL)
        else:
            print(Fore.RED)
            print('{} errors and {} failures so far'.format(len(errors), len(failures)))
            self.log_errors(errors)
            self.log_fails(failures)
            self.save_test_result(test_status={'status': 'FAIL',
                                               'errors': len(errors),
                                               'failures': len(failures),
                                                'hints':self.hints})
            print(Style.RESET_ALL)

    def move_misc_file(self, file_key, filename):
        ff = filename.split('.')

        filename_ts = ff[0] + '_' + self.timestamp + '.' + ff[-1]
        os.system('mv {} {}/{}/{}'.format(filename, self.results_directory, self.test_name, filename_ts))
        self.log_data(file_key, filename_ts)

