import unittest
from colorama import Fore, Style

class TestResult(unittest.runner.TextTestResult):
    def startTest(self, test):
        super(TestResult, self).startTest(test)
        print('\n')
        test_id = test.id().split('.')[-1]
        print(test_id)
        print('-' * len(test_id))
        if test.shortDescription():
            print('Description:\n' + test.shortDescription() + '\n')
        else:
            print(Fore.YELLOW + "[WARNING]: Description Missing for test: {}".format(test_id) + Style.RESET_ALL)

    def stopTest(self, test):
        super(TestResult, self).stopTest(test)
        result = test.defaultTestResult()
        test._feedErrorsToResult(result, test._outcome.errors)
        ok = result.wasSuccessful()
        errors = result.errors
        failures = result.failures

        if ok:
            print(Fore.GREEN)
            print('Test Case passed')
            print(Style.RESET_ALL)
        else:
            print(Fore.RED)
            print('Test Case Failed')
            print('{} errors and {} failures'.format(len(errors), len(failures)))
            print(Style.RESET_ALL)
