import ast
from io import StringIO
import traceback
from thonny import rst_utils
from thonny import get_workbench
import tkinter as tk
from setuptools import find_packages

def format_file_url(filename:str, lineno:int):
    """
    Creates the url allowing to create a hyperlink leading to the right place in the code editor.
    
    Args:
        filename (str): The filename to wich the hyperlink will point
        lineno (int): The corresponding number line of the hyperlink

    Returns:
        str: Returns a hyperlink in RST format. 
    """
    s = "thonny-editor://" + rst_utils.escape(filename).replace(" ", "%20")
    if lineno is not None:
        s += "#" + str(lineno)
    return s

def create_node_representation(node:ast.AST):
    """
    Returns the node representation. Especially returns the prototype or the signature of the node.
    This function can only construct a string representation of the supported nodes. 
    The supported nodes are reported in SourceParser.py in the global variable SUPPORTED_TYPES.
    
    Even if unsupported node is given so just it's name is returned.
    
    Args: 
        node (ast.AST): The supported node 

    Returns:
        str: Return the string represantation of a node
    """
    if isinstance(node, ast.ClassDef):
        return node.name + "(" + ", ".join([a.arg for a in node.bases]) + ")"
    elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return node.name + "(" + ", ".join([a.arg for a in node.args.args]) + ")"
    else:
        return node.name

def get_compilation_error(exc_info:tuple, with_details=True):
    """
    Formats exception information provided by ~exc_info~. If ~with_details~ 
    is True then some details will be given, such as the file name and 
    the line number of the corresponding exception. If False, only the exception 
    type and message are retrieved (the message may include the exception line number).
    
    Args:
        exc_info (tuple): The tuple must contain three elements: 
                        (type, value, traceback) as returned by sys.exc_info().
        with_details (bool): Set as True and some extra informations will be considered
                        while formatting the exception informations. Defaults to True.

    Returns:
        str: Returns a string containing a traceback message for the given ~exc_info~.
    """
    # Get a traceback message.
    excout = StringIO()
    exc_type, exc_val, exc_tb = exc_info
    traceback.print_exception(exc_type, exc_val, exc_tb, file=excout)
    content = excout.getvalue()
    excout.close()
    # la variable `content`` va contenir toute les lignes de la traceback, 
    # mais on en retire que les lignes qui indiquent l'exception renvoyée par l'éditeur thonny
    return __extract_only_error(content.rstrip("\n"), with_details)

def __extract_only_error(traceback_content:str,  with_details:bool):
    """Extract only the lines that represents the compilation error from the traceback content,

    Args:
        content (str): The returned traceback as string.

    Returns:
        str: The lines representing the compilation error 
    """
    # splitted va contenir toutes les ligne de la traceback
    splitted = traceback_content.split("\n")
    keyword = "File"
    exception_index = 0
    # on filtre par le mot "File" pour récupérer le nom du fichier d'où vient l'erreur et sa ligne.
    if with_details:
        for i in range(len(splitted)):
            if keyword in splitted[i]:
                exception_index = i       
        return "\n".join(splitted[exception_index:]).strip()
    else:
        return splitted[-1]
    
def import_module(filename:str):
    """
    Import a module from a given filename. 
    The ~filename~ can be also the absolute path of a file.
    
    This function can raise an exception if the imported module 
    contains a compilation error. You should catch it somewhere.
    
    Args:
        filename (str): The filename(or the absolute path) of a file

    Returns:
        ModuleType: Returns the corresponding module of the given file.
    """
    import importlib.util as iu
    import os, sys
   
    # import the module specification. 
    # To learn more about ModuleSpec `https://peps.python.org/pep-0451/`    
    spec = iu.spec_from_file_location("module.name", filename)
    imported_source = iu.module_from_spec(spec)
    
    workingdir = os.path.split(imported_source.__file__)
    if (len(workingdir) > 0):
        basedir = workingdir[0]
        dirs = get_all_parent_directories(basedir)
        
        # ajout des packages parents au sys.path
        # on fait ça parce que on veut assurer les imports 
        # des fichiers contenant dans les packages parents
        [sys.path.append(path) for path in dirs]
        
        # ajout des sous packages au sys.path 
        # pour assurer les imports des fichiers contenant dans les sous packages
        sub_packages = get_subpackages(basedir)
        [sys.path.append(basedir+os.sep+path) for path in sub_packages]
        
    # this line can raise an exception if the module contains compilation errors
    spec.loader.exec_module(imported_source) 
    return imported_source

def get_all_parent_directories(dir_path:str):
    """
    For a given path of a directcory return all the parents directory from that path.
    
    Examples:
    >>> get_all_parent_directories('/home/stuff/src')
    ['/home', '/home/stuff', '/home/stuff/src']
    """
    import os
    
    if dir_path is None:
        return []
    
    dirs = dir_path.split(os.sep)
    m = ""
    res = []
    for e in dirs[1:]:
        m += os.sep + e  
        res.append(m)
    return res

def get_subpackages(package_path:str):
    """
        Get all sub-packages of a given package(param). 
    """
    return [p.replace(".", "/") for p in find_packages(package_path)]
    

def group_by_node(list_results):
    """Group the tests containing in the ~list_results~ by their nodes.

    Args:
        list_results (List[Test]): a list of Test objects.

    Returns:
        dict: a dictionary containing for each node its list of tests.
    """
    d = dict()
    for test in list_results:
        l = []
        if d.get(test.get_node()):
            l = d[test.get_node()]
        l.append(test)
        d[test.get_node()] = l
    return d

def get_focused_writable_text():
    """
    Returns the focused text

    Returns:
        Widget: A widget Object if there's a focused area in the editor
        None : if no focused area exists in the editor
    """
    widget = get_workbench().focus_get()
    # In Ubuntu when moving from one menu to another, this may give None when text is actually focused
    if isinstance(widget, tk.Text) and (
        not hasattr(widget, "is_read_only") or not widget.is_read_only()
    ):
        return widget
    else:
        return None
    
def selected_test_line(text):
    """
    Get the number of the selected line in the text editor. A None is returned 
    if several lines are selected.
     
    Args:
        text (Widget): The text selected in the text editor. 
                    The value of this parameter must be the result 
                    of invoking the get_focused_writable_text() method. 

    Returns:
        int: The number of the selected line in the text editor.
        None: If several lines are selected.
    """
    # A text is selected in the editor => can't tell the exact line of the test to run
    if len(text.tag_ranges("sel")) > 0:
        return None
    else:
        lineno, _ = map(int, text.index(tk.INSERT).split("."))
    return lineno

def find_node(line, nodes):
    """ Returns a node by its line number.

    Args:
        line (int): The number of the selected line.
        nodes (list(ast.AST)): A list of all ast nodes containing in the text editor. 
                            Must be invoked after an AST parsing.
        
    Returns:
        ast.AST : Returns an AST node if the node was found for the line number
        None : Returns None if no node was found for the line number
    """
    if line == None:
        return None

    for node in nodes:
		# Only functions can be tested separately
		# To be able to test classes and modules separately 
		# remove this condition :
		# isinstance(node, ast.FunctionDef)
		#  ===> if node.lineno == line :
        if node.lineno == line and isinstance(node, ast.FunctionDef) :
            return node
        
def add_random_suffix(word):
    """Add a random suffix to the given word.
     
    The suffix is added in the following format 'word_suffix'. An underscore separates the two words.
    The suffix is assumed to be long(more than 9 caracters).
    
    Args:
        word (str): A word.

    Returns:
        str: Returns the given word with a random suffix appended after an underscore.
    """
    import string
    from random import shuffle, randint
    divider = "_"
    alphabet = list(string.ascii_lowercase + string.ascii_uppercase)
    
    # Divide by three to avoid the first index being so close to the last index.
    # The first index should be smaller than the last index, so we can have a long suffix.
    first_index = randint(0, len(alphabet)//3) 
    last_index = randint(len(alphabet)//2, len(alphabet)-1)
    
    shuffle(alphabet) 
    suffix = "".join(alphabet[first_index: last_index])
    return word + divider + suffix
