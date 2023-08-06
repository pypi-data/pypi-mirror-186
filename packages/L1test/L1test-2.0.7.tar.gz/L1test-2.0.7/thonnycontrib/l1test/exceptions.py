class InterpreterError(Exception): 
    """
    Exception raised when there's a compilation error in the source code.
    """
    pass

class EditorException(Exception):
    """
    exception which includes all exceptions related to the code editor.
    """
    pass
        
class EmptyEditorException(EditorException):
    """
    Exception raised when an editor is still empty. 
    """
    pass

class NotSavedFileException(EditorException):
    """
    Exception raised when an the source code is not saved yet inthe local machine. 
    """
    pass

class NoTestFoundException(EditorException):
    """
    Exception raised when an there's no test in the source code. 
    """
    pass

class NoFunctionSelectedToTest(Exception):
    """
    Exception raised when no function is selected to test. 
    """
    pass

class NoFunctionSelectedToDocument(Exception):
    """
    Exception raised when no function is selected to document. 
    """
    pass
