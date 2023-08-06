from thonny import get_workbench

from ..docstring_generator.DocGenerator import DocGenerator
from .Evaluator import *
from .TestReporter import *
from thonny.ui_utils import select_sequence
from .properties import *

import thonnycontrib.l1test.ThonnyLogsGenerator as LG

from thonnycontrib.l1test.myDoctest import ManqueUnEspace

class TestRunner:
    def __init__(self):
        self.dt_model = Evaluator()
        self.dt_view = TestReporter()
        
    def run(self, selected = False):
        self.clean_error_view()
        has_exception = False
        try:
            test_results = self.dt_model.evaluate(selected)
            self.update_view(test_results)
            LG.log_in_thonny(test_results,selected)
        except EmptyEditorException as e: 
            has_exception = True
            self.dt_view.display_error_msg(str(e))
        except NoTestFoundException as e1:
            has_exception = True
            self.dt_view.display_error_msg(str(e1), prefix_info="", color="orange")
        except NotSavedFileException as e2:  
            has_exception = True
            self.dt_view.display_error_msg(str(e2))
            # We ask the user to save the file first ?
            # self.dt_model.get_editor().save_file()
            #ici
        except ManqueUnEspace as e3_0: # erreur parser doctest, mq un espace après l'invite
            has_exception = True
            self.dt_view.display_error_msg(str(e3_0), color="red")
        except InterpreterError as e3: # parsing error
            has_exception = True
            self.dt_view.display_error_msg(str(e3), color="orange")
        except NoFunctionSelectedToTest as e4:
            has_exception = True
            self.dt_view.display_error_msg(str(e4))

        if (has_exception):
            get_workbench().hide_view("TestTreeView")
            get_workbench().show_view("ErrorView")
        else:
            get_workbench().hide_view("ErrorView")
            get_workbench().show_view("TestTreeView")

    def clean_error_view(self):
        get_workbench().get_view(self.dt_view.error_view.__name__)._clear()
    
    def clean_main_view(self):
        get_workbench().get_view(self.dt_view.main_view.__name__).clear_tree()
                     
    def update_view(self, test_results:dict()):
        """
        Update view according to the ~test_results~.
        """
        self.dt_view.display_tests_results(test_results) 
