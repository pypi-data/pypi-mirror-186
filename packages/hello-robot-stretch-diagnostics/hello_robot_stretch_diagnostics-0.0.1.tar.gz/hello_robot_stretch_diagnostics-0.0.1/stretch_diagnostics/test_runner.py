import unittest
import os
import stretch_body.hello_utils as hu
import yaml
from colorama import Fore, Style
from stretch_diagnostics.test_result import TestResult

class TestRunner(unittest.TextTestRunner):
    resultclass = TestResult

    def __init__(self, suite, doc_verify_fail=False):
        super(TestRunner, self).__init__()
        self.failfast = suite.failfast
        self.suite = suite
        self.doc_verify_fail = doc_verify_fail

    def _suite_verify_doc_fail(self):
        doc_check_fail = False
        if len(self.suite._tests) == 0:
            print(Fore.YELLOW + '[SYSTEM CHECK ERROR]: A test suite must have at least one test\n' + Style.RESET_ALL)
            doc_check_fail = True

        if len(self.suite._tests):
            class_doc = self.suite._tests[0].__doc__
            if class_doc is None:
                print(
                    Fore.YELLOW + '[SYSTEM CHECK ERROR]: A test case must have a class-level docstring' + Style.RESET_ALL)
                doc_check_fail = True

            for t in self.suite._tests:
                if not t.shortDescription():
                    print(Fore.YELLOW + '[SYSTEM CHECK ERROR]: Short Description not provided for test : {}'.format(
                        t.id()) + Style.RESET_ALL)
                    doc_check_fail = True

        return doc_check_fail

    def run(self):
        if self.doc_verify_fail:
            if self._suite_verify_doc_fail():
                print(Fore.RED + 'Stopping Test Run' + Style.RESET_ALL)
                return
        result = super(TestRunner, self).run(self.suite)
        # result = super().run(self.suite)
        if self.suite.test:
            self.suite.test.save_TestResult(result)
        else:
            print(
                Fore.YELLOW + '[WARNING]: Result Data not saved because Test Object was not included with Test Suite.')
            print(
                'Add test object while initializing  "test_suite = TestSuite(Test_XXX_foo.test)" ' + Style.RESET_ALL)
        return result


