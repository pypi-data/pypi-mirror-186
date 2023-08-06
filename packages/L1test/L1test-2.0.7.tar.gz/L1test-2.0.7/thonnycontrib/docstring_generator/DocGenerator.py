import re
import textwrap

from ..l1test.ASTParser import get_supported_nodes

from .DocTemplate import *
from thonny import get_workbench  
from ..l1test.exceptions import NoFunctionSelectedToDocument
from ..l1test.utils import get_focused_writable_text, selected_test_line, find_node
from ..l1test.ThonnyLogsGenerator import log_doc_in_thonny

r""" Docstring Generator Module
Description:
------------
This module generates a docstring using the templates.

Doctring Generator uses the AST module to parse the content of the source code 
and then finds the AST node corresponding to the clicked line. If the selected line 
doesn't refer to any supported AST node(Function, Class) so any docstring 
is generated.

How to use the Generator in thonny IDE:
---------------------------------------
Right click on a function or a class declaration(it's prototype) and choose 
in the `edit menu` ~Generate Docstring~ button. You can also select the short cut 
Alt+d after putting the cursor on the function(or a class) declaration.
  
About templates, the docstring generator invokes the ~DefaultDocTemplate~ by default. 
The DocTemplate.DefaultDocTemplate(DocTemplate) class contains an implementation 
of a default template. 

DocGenerator limitations:
-------------------------
- Always generates a docstring even if a docstring already exists. The old docstring 
isn't removed by the generator. This is problematic because a function(or a class) should
only have one docstring. Maybe the generator shouldn't generate a docstring of a function 
(or class) that already contains a docstring(like other known APIs do).

- For the moment the generation of the doctring is done by clicking 
on the button ~Generate Doctring~ accessible from the menu ~Edit~. In the future, 
the docstring generator should allow automatic generation of the docstring. 
"""

class DocParser:
    def __init__(self):
        # The working editor
        self.editor = get_workbench().get_editor_notebook()
    
    def get_editor_content(self):
        """
        Returns:
            str: returns the content of the current editor
        """
        return self.editor.get_current_editor_content()
                
    def parse_editor_content(self):
        """
        Returns a list of AST nodes that may contains a doctsring.
        
        As the AST python module stated in its documentation, the AST nodes that can 
        contain a dosctring are reported at ~SourceParser.SUPPORTED_TYPES~.
        """
        try :
            return get_supported_nodes(self.get_editor_content())
        except : # if a compilation error occurs during the parsing
            return None     # This is so restrictive and dangereous
        
    def get_editor(self):
        """
        Returns:
            EditorNotebook: Returns the working editor.
        """
        return self.editor
        
class DocGenerator:

    def __init__(self, template:DocTemplate=DefaultDocTemplate()):
        self.parser = DocParser()
        self.template = template
    
    def generate(self):
        """Generate a docstring for a selected line.

        Raises:
            NoFunctionSelectedToDocument: When a selected line don't corresponds to a supported AST node.
                                          A supported AST node is (class, function)
        """
        indent = "    " 
        text = get_focused_writable_text()
        line_number = selected_test_line(text)
        parsed_source = self.parser.parse_editor_content()
        
        # get the content of the selected line
        text_content = text.get(str(line_number)+".0", str(line_number+1)+".0")
        # if an error is occured during source parsing so the parsed_source is None.
        # We generate the minimalist docstring template.
        if not parsed_source :
            # we check if the line corresponds to a function or class declaration 
            if re.match(r"[ \t]*(async[ \t]+)?(?P<type>(def|class){1})[ ]+(?P<name>[\w]+)", text_content):
                # generate a minimalist doctring for the selected node
                text.insert(str(line_number+1) + ".0", textwrap.indent(MinimalistDocTemplate().get_template(node=None), indent))
                return
            else: # otherwise don't generate docstring
                return 
            
        node = self.__find_node(line_number, parsed_source)

        if line_number != None and node != None:
            generated_temp = self.template.get_template(node)
            # c'est içi que la docstring est ajoutée à l'éditeur
            text.insert(str(line_number+1) + ".0", textwrap.indent(generated_temp, indent))
        else : 
            raise NoFunctionSelectedToDocument("No function is selected to document!\n")
        #Generate an event in Thonny with l1test/ThonnyLogsGenerator.log_doc_in_thonny
        log_doc_in_thonny(node)
        
    def __find_node(self, line, nodes):
        """Returns a node by its line number.

        Args:
            line (int): The selected line in the editor
            nodes (list[ast.AST]): List of AST nodes containing in the source code.
                                   The value of this parameter must be the result of calling 
                                   the TestFinder().parse_editor_content() method.

        Returns:
            ast.AST : Returns an AST node if the node was found for the line number
            None : Returns None if no node was found for the line number
        """
        if line == None:
            return None

        for node in nodes:
            if node.lineno == line:
                return node


        
