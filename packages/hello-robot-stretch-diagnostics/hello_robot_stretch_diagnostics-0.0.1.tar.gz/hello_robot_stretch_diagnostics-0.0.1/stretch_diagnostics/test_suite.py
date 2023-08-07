import unittest
from colorama import Fore, Style

class TestSuite(unittest.TestSuite):
    def __init__(self, test=None, failfast=False):
        super().__init__(self)
        self.include_test(test)
        self.failfast = failfast

    def include_test(self, test):
        self.test = test
        if not self.test:
            print(Fore.YELLOW + 'Creating Test Suite Without Test' + Style.RESET_ALL)
