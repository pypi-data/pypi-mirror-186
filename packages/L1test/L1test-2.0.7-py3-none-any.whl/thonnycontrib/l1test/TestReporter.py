import os
import textwrap
import tkinter as tk
from tkinter import PhotoImage, ttk
from thonny import get_workbench, rst_utils, tktextext, ui_utils
from thonny.ui_utils import SafeScrollbar, scrollbar_style

from .properties import PLUGIN_NAME

from .classe.EmptyTest import EmptyTest
from .classe.ExceptionTest import ExceptionTest
from .classe.FailedTest import FailedTest
from .classe.PassedTest import PassedTest
from .utils import *

images=[]

class TestTreeView(ttk.Frame):    
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self._init_widgets(master)

    def _init_widgets(self, master):
        # init and place scrollbar
        self.vert_scrollbar = SafeScrollbar(self, orient=tk.VERTICAL)
        self.vert_scrollbar.grid(row=0, column=1, sticky=tk.NSEW)

        # ajout ici
        self.horz_scrollbar = SafeScrollbar(self, orient=tk.HORIZONTAL)
        self.horz_scrollbar.grid(row=1, column=0, sticky=tk.NSEW)
        
        
        # init and place tree
        # changé ici
        #self.tree = ttk.Treeview(self, yscrollcommand=self.vert_scrollbar.set)
        self.tree = ttk.Treeview(self, yscrollcommand=self.vert_scrollbar.set, xscrollcommand=self.horz_scrollbar.set)
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)
        self.vert_scrollbar["command"] = self.tree.yview
        # ajout ici
        self.horz_scrollbar["command"] = self.tree.xview
        
        # set single-cell frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # init tree events
        self.tree.bind("<<TreeviewSelect>>", self._on_select, True)

        # configure the only tree column
        # ajout ici
        self.tree.column("#0", anchor=tk.W, width = 100, stretch=True)
        #        self.tree.column("#0", anchor=tk.W, stretch=True)
        # self.tree.heading('#0', text='Item (type @ line)', anchor=tk.W)
        self.tree["show"] = ("tree",)

        self.tree.tag_configure('orange', foreground='orange')
        self.tree.tag_configure('red', foreground='red')
        self.tree.tag_configure('green', foreground='darkgreen')

        ttk.Style().configure('Treeview',rowheight=40)
        
        # le chemin c'est par rapport au dossier /l1test 
        # donc il faut remonter vers /thonnycontrib/ pour rentrer dans docs/res
        parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        
        self.passed_img = tk.PhotoImage(file=os.path.join(parent_dir, "docs/res", "passed.png"))
        self.failed_img = tk.PhotoImage(file=os.path.join(parent_dir, "docs/res", "failed.png"))
        self.warning_img = tk.PhotoImage(file=os.path.join(parent_dir, "docs/res", "warning.png"))

        images.append(self.passed_img)
        images.append(self.failed_img)
        images.append(self.warning_img)

    
    def update_frame_contents(self, results:dict):
        self.clear_tree()

        editor = get_workbench().get_editor_notebook().get_current_editor()
        if editor is None:
            return

        for node, tests in results.items():
            self._add_item_to_tree("", node, tests)
        
        # Empty row is added to seperate the test results from the report
        self.tree.insert("", "end", text="")
        # report the summary as the last element of the tree
        self.tree.insert("", "end", text=self.summarize(results))

    def __calculate_function_status(self, tests):
        if any([isinstance(test, FailedTest) or isinstance(test, ExceptionTest) for test in tests]):
            return "failed"
        elif all([isinstance(test, PassedTest) for test in tests]):
            return "passed"
        return "warning"

    def wrap(string, lenght=8):
        return '\n'.join(textwrap.wrap(string, lenght))

    def summarize(self, results:dict):
        TEST_RUNS, FAILURES, ERRORS, EMPTY = "Tests Run: ", "Failures: ", "Errors: ", "Empty: "
        
        test_run = TEST_RUNS + str(sum([1 for _, tests in results.items() 
                                                for t in tests if not isinstance(t, EmptyTest)]))
        
        failures = FAILURES + str(sum([1 for _, tests in results.items() 
                                                for t in tests if isinstance(t, FailedTest)]))
        
        errors = ERRORS + str(sum([1 for _, tests in results.items() 
                                            for t in tests if isinstance(t, ExceptionTest)]))
        
        empty_test = EMPTY + str(sum([1 for _, tests in results.items()
                                                    for t in tests if isinstance(t, EmptyTest)]))

        return "%s, %s, %s, %s\n" %(test_run, failures, errors, empty_test)
        
    # adds a single item to the tree, recursively calls itself to add any child nodes
    def _add_item_to_tree(self, parent, item, tests):
        # create the text to be played for this item
        item_text = " " + create_node_representation(item)
        status = self.__calculate_function_status(tests)

        # insert the item, set lineno as a 'hidden' value
        if (status == 'failed'):
            current = self.tree.insert(parent, "end", text=item_text, open=True, image = self.failed_img, values=item.lineno)

        elif (status == 'passed'):
            current = self.tree.insert(parent, "end", text=item_text, image = self.passed_img, values=item.lineno)

        else :
            current = self.tree.insert(parent, "end", text=item_text, image = self.warning_img, values=item.lineno)

        for test in tests:
            item_text = " " + str(test)
            if isinstance(test, FailedTest) or isinstance(test, ExceptionTest):
                current_test = self.tree.insert(current, "end", text=item_text, open=True, values=test.get_lineno(), tags=test.get_tag())
                # a failure message can be reported on several line, so we should add as many rows as text lines. 
                self.__add_as_many_rows_as_text_lines(current_test, test.get_detail_failure(), test.get_lineno(), test.get_tag())
            else :
                current_test = self.tree.insert(current, "end", text=item_text, values=test.get_lineno(), tags=test.get_tag())
        
    def __add_as_many_rows_as_text_lines(self, parent, text:str, lineno:int, tag:str):
        splitted = text.split("\n")
        for line in splitted:
            self.tree.insert(parent, "end", text=line, values=lineno, tags=tag) 
                   
    # clears the tree by deleting all itemsopen=True
    def clear_tree(self):
        for child_id in self.tree.get_children():
            self.tree.delete(child_id)

    def _on_select(self, event):
        editor = get_workbench().get_editor_notebook().get_current_editor()
        if editor:
            code_view = editor.get_code_view()
            focus = self.tree.focus()
            if not focus:
                return

            values = self.tree.item(focus)["values"]
            if not values:
                return

            lineno = values[0]
            index = code_view.text.index(str(lineno) + ".0")
            code_view.text.see(index)  # make sure that the double-clicked item is visible
            code_view.text.select_lines(lineno, lineno)

            get_workbench().event_generate(
                "OutlineDoubleClick", item_text=self.tree.item(self.tree.focus(), option="text")
            )

class ErrorView(tktextext.TextFrame):
    def __init__(self, master):
        tktextext.TextFrame.__init__(
            self,
            master,
            text_class=AssistantRstText,
            vertical_scrollbar_style=scrollbar_style("Vertical"),
            horizontal_scrollbar_style=scrollbar_style("Horizontal"),
            horizontal_scrollbar_class=ui_utils.AutoScrollbar,
            read_only=True,
            wrap="word",
            font="TkDefaultFont",
            # cursor="arrow",
            padx=5,
            pady=5,
            insertwidth=0,
        )
        
        self.text.tag_config("green", foreground="darkgreen")
        self.text.tag_config("red", foreground="red")
        self.text.tag_config("orange", foreground="orange")
        self.text.tag_config("yellow", foreground="yellow")

    def _append_text(self, chars, tags=()):
        self.text.direct_insert("end", chars, tags=tags)

    def write(self, data):
        self.text.set_content(data)

    def append_rst(self, rst, global_tags=()):
        self.text.append_rst(rst, global_tags)

    def _clear(self):
        self.write("")
        
class TestReporter():
    CANNOT_RUN_TESTS_MSG = "Cannot run %s:" %(PLUGIN_NAME)
    
    def __init__(self, main_view=TestTreeView, error_view=ErrorView):
        self.error_view = error_view
        self.main_view = main_view
    
    def display_error_msg(self, error_msg:str, prefix_info=CANNOT_RUN_TESTS_MSG, color="orange"):
        if prefix_info:
            get_workbench().get_view(self.error_view.__name__)._append_text(prefix_info+"\n", tags="red")
        get_workbench().get_view(self.error_view.__name__)._append_text(error_msg, tags=color)
                                  
    def display_tests_results(self, results):
        get_workbench().get_view(self.main_view.__name__).update_frame_contents(results)
        
class AssistantRstText(rst_utils.RstText):
    def configure_tags(self):
        super().configure_tags()

        main_font = tk.font.nametofont("TkDefaultFont")

        italic_font = main_font.copy()
        italic_font.configure(slant="italic", size=main_font.cget("size"))

        h1_font = main_font.copy()
        h1_font.configure(weight="bold", size=main_font.cget("size"))

        self.tag_configure("h1", font=h1_font, spacing3=0, spacing1=10)
        self.tag_configure("topic_title", font="TkDefaultFont")

        self.tag_configure("topic_body", font=italic_font, spacing1=10, lmargin1=25, lmargin2=25)

        self.tag_raise("sel")

        
        
