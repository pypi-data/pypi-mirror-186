# Module Evaluator

from ast import get_docstring

from .exceptions import *

from .utils import *
from .myDoctest import *
from thonny import get_workbench
        
from .ASTParser import *
import sys

from .classe.EmptyTest import EmptyTest
from .classe.PassedTest import PassedTest
from .classe.FailedTest import FailedTest
from .classe.ExceptionTest import ExceptionTest


class TestFinder:

    def __init__(self):
        WORKBENCH = get_workbench()
        EDITOR_NOTEBOOK = None if WORKBENCH is None else WORKBENCH.get_editor_notebook()
        # The working editor
        self.editor = EDITOR_NOTEBOOK
        # The filename includes it's path
        # If there's no editor opened -> set the filename to null to avoid the null exception
        # l'exec de la ligne suivante ne rend pas la main
        if self.editor is None:
            self.filename = None
        elif self.editor.get_current_editor() is None:
            self.filename = None
        else:
            self.filename = self.editor.get_current_editor().save_file()

    
    def get_editor_content(self):
        """
        Returns the content of the current editor.
        This function does not directly return the contents of an editor, 
        it performs checks in the following order:
        1- Checks if a text editor is open on thonny. 
            Otherwise throws the exception that no editor is open.
        2- Checks if the file corresponding to the editor is previously registered in the file system. 
            Otherwise an exception is thrown to indicate that the file must be registered 
            somewhere in the file system of a machine.
        3- Checks if the content of the editor is empty. 
            Otherwise, throws an exception that the file is empty.
        After all these checks pass the content of the editor is returned.
        
        Raises:
            EmptyEditorException: when the editor is still empty or when there's no opened editor.
            NotSavedFileException: When the editor is not saved yet in a local file.
        Returns:
            str: returns the content of the current editor
        """
        content:str = self.editor.get_current_editor_content()
        if self.editor.get_current_editor() is None:
            raise EmptyEditorException("No editor is open yet! An editor should already be opened.\n")
        if self.filename is None:
            raise NotSavedFileException("The source code must be saved in a file!\n")
        if not content.strip():
            raise EmptyEditorException("The editor is empty!\n")      
        return content
    
    def parse_editor_content(self):
        """
        Returns a list of AST nodes that may contains a doctsring.
        
        As the AST python module stated in its documentation, the AST nodes that can 
        contain a dosctring are reported at ~SourceParser.SUPPORTED_TYPES~.
        """
        try :
            return get_supported_nodes(self.get_editor_content())
        except :
            e = sys.exc_info()[1]
            raise InterpreterError(e)

    
    def __filter_example_instances(self, parsed_doc:list):
        """
        The filter can return an empty list if there's no example 
        in the parsed docstring.
        """
        return [s for s in parsed_doc if isinstance(s, Example)]
        
    def extract_examples(self, selected):
        """
        Extract examples from the docstings of all the ast nodes of the source code.
        
        Returns a dictionary containing for each supported ast node  
        it's list of examples(the list may be empty if no tests detected in a docstring).
        exam[1]==parsed_doc[1]
        """
        docstrings = None
        if (selected):
            docstrings = get_docstring(self.parse_editor_content())
        else :
            docstrings = get_all_docstrings(self.parse_editor_content())       
        node_examples = {}
        for node, docstring in docstrings.items():
            # if a dosctring of a node is null or empty so there's nothing to parse
            if docstring is None or not docstring.strip():
                node_examples[node] = []
            else:
                parsed_doc = DocTestParser().parse(docstring)
                node_examples[node] = self.__filter_example_instances(parsed_doc)
        return node_examples
    
    def nodes_have_examples(self, extracted_tests:dict):
        """
        Returns a dictionary containing for each supported ast node if it has examples or not(bool)
        """
        return dict([(node, len(examples)>0) for (node, examples) in extracted_tests.items()])
    
    def node_have_examples(self, node, extracted_tests:dict):
        """
        Returns true if a node contains at least one test. False otherwise
        """
        return self.__count_node_example_tests(node, extracted_tests) > 0
    
    def __count_node_example_tests(self, node, extracted_tests:dict):
        """
        Returns the number of example tests of a node.
        Specifically, returns 0 if there's no test in the given node.
        Returns -1 if the given node don't exist.
        """
        nodes = self.nodes_have_examples(extracted_tests)
        if node in nodes:
            return nodes[node]
        else:
            return False
    
    def contains_examples(self, extracted_tests:dict):
        """
        Returns True if the source code contains at least one example test. 
        Returns False otherwise.
        """
        return any(list(self.nodes_have_examples(extracted_tests).values()))

    def get_filename(self):
        """
        Returns:
            (str) : Returns the filename of the working editor. The filename includes it's full path.
        """
        return self.filename
        
class Evaluator:
    
    def __init__(self, test_finder=TestFinder):
        self.local_variables = dict()
        self.globals = dict()
        self.test_finder:TestFinder = test_finder()

        
    def execute_source(self, source:str, globals:dict, locals:dict, mode="exec"):
        """
        Execute a source code using the given globals. 
        Args:
            source (str): A string representing a source code. 
            globals (dict): The dictionary of the global variables.
            locals (dict): The dictionary of the local variables. 
            mode (str): The mode in which the source will be compiled by the compiler. 
                        - `exec` mode: to compile a whole source code.
                        - `single` mode: to compile a single (interactive) statement.
        Raises:
            InterpreterError: When the source code contains an error like SyntaxError, NameError ... 
        """
        try:
            exec(compile(source, filename=self.test_finder.filename, mode=mode), globals, locals)
        except:
            error_info = sys.exc_info()
            formatted_error = get_compilation_error(error_info, False)
            raise InterpreterError(formatted_error)

    def evaluate(self, selected):
        """
        Evaluate all the tests containing in the working editor. 
        Returns a list of passed, failed or empty tests. 
        The list can also contains the tests that raises other exceptions.
        
        Args:
            selected (bool): Set as True if a node is selected, so we must only 
                             evaluate its examples. 

        Raises:
            NoTestFoundException: When no test are found in the working editor
            EmptyEditorException: When the editor is empty and doesn't contain the code.
        """
        test_results = []
        
        try:
            # import the module corresponding to the working filename
            # the import_module function can raise an exception(see it's doc)
            module = import_module(self.test_finder.get_filename())
        except Exception as e:
            # the compilation error is catched and raised as an InterpreterError
            # and the evaluation is interrupted(because we cannot parse a content
            # with compilation errors).
            error_info = sys.exc_info()
            formatted_error = get_compilation_error(error_info)
            raise InterpreterError(formatted_error)
        
        extracted_tests = self.test_finder.extract_examples(selected) 

        # set a globals dictionary that will contains all the functions and 
        # meta-informations decalared in the module
        self.globals = module.__dict__
        
        if self.test_finder.contains_examples(extracted_tests) or selected: 
            for node, examples in extracted_tests.items():
                self.clear_local_variables()       
                if self.test_finder.node_have_examples(node, extracted_tests):

                    for example in examples: 
                        source, want = example.source, example.want
                        example_line = node.lineno + example.lineno + 1
                        if not want: # if there's no expected result -> execute the statement   
                            try:  
                                self.execute_source(source, self.globals, self.local_variables)
                            except InterpreterError as error:
                                verdict = ExceptionTest(self.test_finder.get_filename(), node=node, tested_line=source.strip(), 
                                                        expected_result=want.strip(), lineno=example_line, exception=str(error))
                                test_results.append(verdict)
                        else: # if we are here so there's an expected result -> comparing results      
                            final_verdict = self.__exec_and_compare_results(source, want, example_line, node)                  
                            test_results.append(final_verdict)
                else:
                    test_results.append(EmptyTest(self.test_finder.get_filename(), node=node, lineno=node.lineno))
                                
        else:
            raise NoTestFoundException("There's no doctest in the source code!\n")
        return group_by_node(test_results)
                        
    def __exec_and_compare_results(self, source:str, want:str, lineno:int, node:ast.AST):
        """
        Compare the source and the wanted value of a node. The result is added to the ~res~ list.
        
        Args:
            source (str): the source statement to execute(or to test).
            want (str): The wanted value.
            lineno (int): The number line of the test in a given node.
            node (ast.AST): The node that contains the example.
        
        Returns: 
            Test: returns the verdict that corresponds to the result of the comparison of want with got.
        """
        executed, wanted = add_random_suffix("executed"), add_random_suffix("wanted")   
        try:
            compile(self.str_comparaison(source, want), self.test_finder.filename, "single")
            exec(executed+"="+source, self.globals, self.local_variables)
            exec(wanted+"="+want, self.globals, self.local_variables)
            if self.local_variables[executed] == self.local_variables[wanted]:
                verdict = PassedTest(self.test_finder.get_filename(), node=node, tested_line=source.strip(), 
                                      expected_result=want.strip(), lineno=lineno)
            else:
                verdict = FailedTest(self.test_finder.get_filename(), node=node, tested_line=source.strip(), 
                                      expected_result=want.strip(), obtained_result=str(self.local_variables[executed]), 
                                      lineno=lineno)
        except: # catch *all* error / exceptions
            type, value, traceback = error = sys.exc_info()
            if(str(type.__name__) == want.strip("\n")):
                verdict = PassedTest(self.test_finder.get_filename(), node=node, tested_line=source.strip(), 
                                      expected_result=want.strip(), lineno=lineno)
            else:
                verdict = ExceptionTest(self.test_finder.get_filename(), node=node, tested_line=source.strip(), 
                                        expected_result=want.strip(), lineno=lineno, 
                                        exception=get_compilation_error(error, False))
        return verdict
    
    def str_comparaison(self, expected, got):
        return '(' + expected + ') == (' + got + ')'

    def clear_local_variables(self):
        self.local_variables.clear()
        
    def set_test_finder(self, test_finder):
        self.test_finder = test_finder

