import ast

from .exceptions import NoFunctionSelectedToTest

from .utils import *

# Only these types can have a docstring 
# according to ast's module documentation
SUPPORTED_TYPES = (ast.FunctionDef, 
                   ast.AsyncFunctionDef, 
                   ast.ClassDef, 
                   ast.Module)

    
def get_supported_nodes(source_content:str):
    """
        Get only the nodes that can have a docstring. 
        The supported nodes are repported to ~SUPPORTED_TYPES~ constant.
    """
    source_nodes = [node for node in get_body(source_content) if isinstance(node, SUPPORTED_TYPES)]
    all_nodes = []
    # get all the supported nodes from a source content
    __recursive_walking(source_nodes, all_nodes)
    return all_nodes

def parse(source_content:str):
    """
    Get the AST tree of a source code ~source_content~.
    Returns AST.Module the root node of the AST tree.
    """
    return ast.parse(source_content)

def get_body(source_content:str):
    """
    Returns the body(list of nodes) of the root node of the AST tree.
    """
    return parse(source_content).body

def get_fields(node:ast.AST):
    """
    Takes a AST node and returns a dictionary containing for each field name 
    of the noe its value.
    """
    return dict([(field_name, child_node) 
                    for (field_name, child_node) in ast.iter_fields(node)])

def get_all_docstrings(list_nodes:list):
    """
    Takes a list of supported nodes and returns a dictionary 
    containing for each supported type its docstring
    """
    return dict([(node, ast.get_docstring(node, False)) for node in list_nodes])

def get_docstring(list_nodes:list):
    """
    Returns a dictionary containing the node and its docstring
    for the node that exists on the selected line
    """
    line_number = selected_test_line(get_focused_writable_text())
    node = find_node(line_number, list_nodes)

    if line_number != None and node != None:
        return dict([(node, ast.get_docstring(node, False))])
    else : 
        raise NoFunctionSelectedToTest("No function is selected to test !\n")

def __recursive_walking(list_nodes:list, all_nodes:list):
    """
    Search all the supported nodes in the AST tree. Even sub-nodes are visited.
    This is a recursive function, so all the visited nodes are added in the ~all_nodes~
    parameter.
    """
    for node in list_nodes:
        if isinstance(node, SUPPORTED_TYPES):
            all_nodes.append(node)
            __recursive_walking(node.body, all_nodes)
