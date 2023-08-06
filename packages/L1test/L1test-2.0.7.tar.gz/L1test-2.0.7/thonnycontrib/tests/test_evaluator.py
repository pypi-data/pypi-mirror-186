# classe de test initiale et unique de Reda et Manal (PJI L3 2022)
# compliqué à lire 


import unittest as ut

from l1test.Evaluator import Evaluator, TestFinder
from l1test.exceptions import *
from l1test.classe.EmptyTest import EmptyTest
from l1test.classe.ExceptionTest import ExceptionTest
from l1test.classe.FailedTest import FailedTest
from l1test.classe.PassedTest import PassedTest
from l1test.TestReporter import TestTreeView

class MockTestFinder(TestFinder):
    FAKE_CONTENT = ""
    
    def get_editor_content(self):
        return self.FAKE_CONTENT
     
    def set_FAKE_CONTENT(self):
        f = open(self.get_filename(), "r")
        self.FAKE_CONTENT = f.read()
        f.close()
        
    def set_filename(self, filename):
        self.filename = filename

class MockTestReporter(TestTreeView):
    def __init__(self):

        self.is_invoked = False
    
    def summarize(self, results:dict):
        self.is_invoked = True
        return super().summarize(results)
    
class FakeTestFixture:
    __EXAMPLE = \
"""
def f(a, b):
    \"""
    %s
    \"""
    if a < 0 and b < 0:
        return None
    return a + b
"""
    EMPTY_EXAMPLE = \
"""
def g(a, b):
    return a - b
"""
    FILENAME = "dump_tests.py"
    
    def __init__(self):
        self.example = self.__EXAMPLE
        
    def create_fake_examples(self, how_many):
        examples = "%s\n    " %("%s") * how_many
        self.example = self.example % (examples)
        
    def add_fake_test(self, source, want):
        self.example = self.example %(source, want)
    
    def save_fake_example(self, examples, node:str=None):
        self.example = self.__EXAMPLE
        self.create_fake_examples(len(examples)*2)
        for (source, want) in examples:
            self.add_fake_test(source, want)
        self.write_example_in_file(self.example)
    
    def write_example_in_file(self, txt):
        a = open(self.FILENAME, "a")
        a.write(txt)
        a.close()
    
    def clean(self):
        import os
        self.example = self.__EXAMPLE
        if os.path.exists(self.FILENAME):
            os.remove(self.FILENAME)
        else:
            pass
    
class TestEvaluator(ut.TestCase):
    
    def setUp(self):
        self.mock_test_finder = MockTestFinder()
        self.test_fixture = FakeTestFixture()
        self.evaluator = Evaluator(self.mock_test_finder.__class__)
        
    def tearDown(self):
        self.test_fixture.clean()
    
    def test_passed_case(self):
        (source, want) = "$py f(1, 2)", "3"
        self.test_fixture.save_fake_example([(source, want)])
        verdict = self.__get_verdicts()
        self.__verify_test(verdict, PassedTest)
    
    def test_failed_case(self):
        (source, want) = "$py f(1, 2)", "2"
        self.test_fixture.save_fake_example([(source, want)])
        verdict = self.__get_verdicts()
        self.__verify_test(verdict, FailedTest)  
    
    def test_exception_case(self):
        source, want = ("$py f('j', 2)", "2")
        self.test_fixture.save_fake_example([(source, want)])   
        verdict = self.__get_verdicts()
        self.__verify_test(verdict, ExceptionTest)
    
    def test_none_case(self):
        (source, want) = "$py f(-1, -1)", "None"
        self.test_fixture.save_fake_example([(source, want)])
        verdict = self.__get_verdicts()
        self.__verify_test(verdict, PassedTest)
                  
    def test_setup_without_want(self):
        (source, want) = "$py l = []", ""
        self.test_fixture.save_fake_example([(source, want)])
        verdict = self.__get_verdicts()
        # it's just a setup -> no verdict
        self.__verify_test(verdict, [])
           
    def test_setup_with_a_want(self):
        (source, want) = "$py l = []", "[]"
        self.test_fixture.save_fake_example([(source, want)]) 
        verdict = self.__get_verdicts()
        self.__verify_test(verdict, ExceptionTest)
        
    def test_when_all_empty_tests(self):
        (source, want) = "", ""
        self.test_fixture.save_fake_example([(source, want)])
        with self.assertRaises(NoTestFoundException):
            self.__get_verdicts()
    
    def test_when_some_empty_tests(self):
        (source, want) = "$py f(1, 1)", "2"
        self.test_fixture.save_fake_example([(source, want)])
        self.test_fixture.write_example_in_file(self.test_fixture.EMPTY_EXAMPLE)
        verdicts = self.__get_verdicts()
        self.__verify_test(verdicts, [PassedTest, EmptyTest])
    
    def test_when_syntax_error(self):
        (source, want) = "$py f(1, 1", "2"
        self.test_fixture.save_fake_example([(source, want)])
        verdicts = self.__get_verdicts()
        self.__verify_test(verdicts, ExceptionTest)
        self.assertTrue(SyntaxError.__name__ in verdicts[0].get_exception())
                           
    def __get_verdicts(self):
        self.mock_test_finder.set_filename(self.test_fixture.FILENAME)
        self.mock_test_finder.set_FAKE_CONTENT()
        self.evaluator.set_test_finder(self.mock_test_finder)
        return [v for _, verdicts in self.evaluator.evaluate(selected=False).items() for v in verdicts]
        
    def __verify_test(self, verdicts, expected):
        if not isinstance(expected, list): 
            expected = [expected]
        self.assertTrue(len(verdicts) == len(expected))
        if verdicts:
            for i in range(len(verdicts)):  
                self.assertEqual(verdicts[i].__class__, expected[i])

class TestTestReporter(ut.TestCase):
    def setUp(self):
        self.mock_test_finder = MockTestFinder()
        self.test_fixture = FakeTestFixture()
        self.evaluator = Evaluator(self.mock_test_finder.__class__)
        self.mock_test_reporter = MockTestReporter()
        
    def tearDown(self):
        self.test_fixture.clean()
    
    def test_summarize(self):
        # save a passed test case
        (source, want) = "$py f(1, 1)", "2"
        self.test_fixture.save_fake_example([(source, want)])
        
        # save a failed test case
        (source, want) = "$py f(1, 1)", "3"
        self.test_fixture.save_fake_example([(source, want)])
        
        # save an exception(syntax error) test case
        (source, want) = "$py f(1, 1", "3"
        self.test_fixture.save_fake_example([(source, want)])
        
        # save a setup (a "test" without a <want>), so it will be just executed and no verdict is given   
        (source, want) = "$py l = []", ""
        self.test_fixture.save_fake_example([(source, want)])
        
        # save an empty test case
        self.test_fixture.write_example_in_file(self.test_fixture.EMPTY_EXAMPLE)
        
        # création des verdicts attendu et leurs couleurs
        from collections import OrderedDict
        expected_verdicts = OrderedDict()
        expected_verdicts[PassedTest] = "green"
        expected_verdicts[FailedTest] = "red"
        expected_verdicts[ExceptionTest] = "red"
        expected_verdicts[EmptyTest] = "orange"

        # vérfication des verdicts dans l'ordre des tests 
        verdicts_each_node = self.__get_verdicts_of_each_node()
        only_verdicts = [v for _, verdicts in verdicts_each_node.items() for v in verdicts]
        self.__verify_test(only_verdicts, list(expected_verdicts.keys()))
        
        # verification des couleurs des verdicts dans l'ordre des tests
        self.__verify_colors_tags(list(expected_verdicts.values()), only_verdicts)
        
        # vérification du summarize = le rapport final affiché en bas de la view
        summarize = self.mock_test_reporter.summarize(verdicts_each_node)
        self.assertTrue(self.mock_test_reporter.is_invoked)
        
        from collections import namedtuple
        TEST_RUNS, FAILURES, ERRORS, EMPTY = "Tests_Run", "Failures", "Errors", "Empty"
        expected_summarize = namedtuple('expected_summarize', [TEST_RUNS, FAILURES, ERRORS, EMPTY])
        values_summarize = expected_summarize(3, 1, 1, 1)
        expected = "%s: %s, " %(TEST_RUNS.replace("_", " "), values_summarize.Tests_Run) +\
                   "%s: %s, " %(FAILURES, values_summarize.Failures) +\
                   "%s: %s, " %(ERRORS, values_summarize.Errors) +\
                   "%s: %s\n" %(EMPTY, values_summarize.Empty)
        self.assertEqual(expected, summarize)
    
    def __get_verdicts_of_each_node(self):
        self.mock_test_finder.set_filename(self.test_fixture.FILENAME)
        self.mock_test_finder.set_FAKE_CONTENT()
        self.evaluator.set_test_finder(self.mock_test_finder)
        return self.evaluator.evaluate(selected=False)
        
    def __verify_test(self, verdicts, expected):
        if not isinstance(expected, list): 
            expected = [expected]
        self.assertTrue(len(verdicts) == len(expected))
        if verdicts:
            for i in range(len(verdicts)):  
                self.assertEqual(verdicts[i].__class__, expected[i])

    def __verify_colors_tags(self, expected_colors, verdicts):
        self.assertTrue(len(verdicts) == len(expected_colors))
        if verdicts:
            for i in range(len(verdicts)):  
                self.assertEqual(verdicts[i].get_tag(), expected_colors[i])
                
if __name__ == '__main__':
    ut.main()   
        
