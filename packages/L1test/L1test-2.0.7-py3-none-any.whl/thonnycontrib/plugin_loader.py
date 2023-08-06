import os.path
from thonny import get_workbench
from thonny.ui_utils import select_sequence
from thonnycontrib.docstring_generator.DocGenerator import DocGenerator
from thonnycontrib.l1test.TestReporter import ErrorView, TestTreeView
from thonnycontrib.l1test.TestRunner import TestRunner
from thonnycontrib.l1test.exceptions import NoFunctionSelectedToDocument
from thonnycontrib.l1test.properties import PLUGIN_NAME

from thonnycontrib.l1test.utils import get_focused_writable_text

def run_all_tests():
    controller = TestRunner()
    controller.run()

def run_test():
    controller = TestRunner()
    controller.run(True)

        
def generate_docstring():
    docgen = DocGenerator()
    try:
        docgen.generate()
    except NoFunctionSelectedToDocument as e:
        return # do nothing. we don't generate anything if a selected line is not a function.


    
def _writable_text_is_focused():
    """
    Returns:
        boolean: Returns True if the selected zone is a writable text.
    """
    return get_focused_writable_text() is not None
    
def load_plugin():
    """
    load_plugin est un nom de fonction spécifique qui permet à thonny de charger les élements du plugin
    """
    get_workbench().add_view(TestTreeView, PLUGIN_NAME, "nw", visible_by_default=True)
    get_workbench().add_view(ErrorView, 'L1Test error log', "sw", visible_by_default=False)
    
    image_path = os.path.join(os.path.dirname(__file__), "docs/res", "l1test_icon.png")
    # Création du bouton pour lancer notre plugin de test  
    get_workbench().add_command(command_id=PLUGIN_NAME,
                                menu_name="tools",  
                                command_label=PLUGIN_NAME,
                                handler=run_all_tests,#_in_thread, #lors de l'appui sur le bouton la fonction rundoctest est lancé 
                                include_in_toolbar=True, #j'inclue ici ce bouton dans la toolbar 
                                image=image_path,
                                caption=PLUGIN_NAME)

    
    # Création du bouton dans le menu 'Edit' pour lancer un seul test d'une seul foncton
    get_workbench().add_command(
                                command_id="function test",
                                menu_name="edit",  
                                command_label="Run test for selected function",
                                handler=run_test, #lors de l'appui sur le bouton la fonction rundoctest est lancé  
                                tester=_writable_text_is_focused
    )
    
    # Création du bouton dans le menu 'Edit' pour lancer la Docstring Generator
    get_workbench().add_command(
                                command_id="doc_generator",
                                menu_name="edit",  
                                command_label="Generate a docstring",
                                handler=generate_docstring, 
                                tester=_writable_text_is_focused,
                                default_sequence=select_sequence("<Alt-d>", "<Command-Alt-d>", "<Alt-d>"),
                                accelerator="Alt+d"
    )



