# Auteur : Esteban COLLARD, Nordine EL AMMARI
# Refactored by Manal LAGHMICH & Réda ID-TALEB
import ast

from ..utils import format_file_url

class Test():
    
    def __init__(self, filename:str, node:ast.AST, tested_line:str, expected_result:str, lineno:int):
        """
        Build an instance of a test. A the Test object represents a result of a 
        tested line in a docstring.
        
        Args:
            filename (str): The filename in wich the tests are run.
            node (ast.AST): The AST node corresponding to the tested line.
            tested_line (str): The tested line.
            expected_result (str): The expected result of the tested line
            lineno (int): The line number of the tested line.
        """
        self.filename = filename
        self.node = node
        self.tested_line = tested_line
        self.expected_result = expected_result
        self.lineno = lineno

    def get_node(self):
        return self.node

    def get_tested_line(self):
        return self.tested_line

    def get_expected_result(self):
        return self.expected_result

    def get_filename(self):
        return self.filename
    
    def get_lineno(self):
        return self.lineno
    
    def get_tag(self):
        return ""
    
    def get_hyperlien_of_test(self):
        return "`line %d <%s>`__ %s" % (self.lineno, format_file_url(self.filename, self.lineno), "")
    
    def __str__(self):
        if self.expected_result:
            return 'Trying: %s\n\n' %(self.tested_line) + 'Expecting: %s\n\n' %(self.expected_result)
        return 'Trying: %s\n\n' %(self.tested_line) + 'Expecting nothing.\n\n'
