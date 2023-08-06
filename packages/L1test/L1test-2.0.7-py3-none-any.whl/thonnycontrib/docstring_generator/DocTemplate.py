from abc import *
import ast

class DocTemplate(ABC):
    # Ces constantes peuvent être utilisées dans les classes d'implémention
    NEW_LINE = "\n"
    DOCSTRING_SYMBOL = '"""'
    
    @abstractmethod
    def _format_general_summary(self):
        """
        Returns:
            str: Returns a label which will indicate to write a summary of the function.
        """
        pass
    
    @abstractmethod
    def _format_params(self, params):
        """
        Args:
            params (List): It's a list of the arguments.

        Returns:
            str: Returns the parameter representation section of a node in a docstring. 
        """
        pass
    
    @abstractmethod
    def _format_usage_constraints(self):
        """
        Returns:
            str: Returns the usage constraints representation section in a docstring.
        """
        pass
    
    @abstractmethod
    def _format_return_value(self):
        """
        Returns:
            str: Returns the return value representation section in a docstring.
        """
        pass
    
    @abstractmethod
    def _format_test_examples(self):
        """
        Returns:
            str: Returns the test examples representation section in a docstring.
        """
        pass
    
    @abstractmethod
    def get_template(self, node:ast.AST):
        """Build the complete docstring template. 
        This method must invoke the above abstract methods.
        
        Args:
            node (ast.AST): The AST node in which the dosctring will be generated.

        Returns:
            str: Returns the template representation. 
        """
        pass
    
class DefaultDocTemplate(DocTemplate):
    '''
    Modifié pour coller au cours d'Info L1
    '''
    # Les mots utilisés dans le template par défault
    TODO_LABEL = "" #"__à compléter__"
    
    SUMMARY_LABEL = "x_résumé_x"
    PARAM_LABEL = "Paramètres :" 
    CU_LABEL = "Contraintes d'utilisation : "
    RETURN_LABEL = "Valeur de retour " 
    RETURN_TYPE_LABEL = "() :" #"__type de retour ?__ (%s)%s"
    DOCTEST_LABEL = "Exemples :\n$$$ "
    
    def get_parameters(self, node:ast.AST):
        """
        Get the paramters of a given node.
        
        Args:
            node (ast.AST): An AST node. Must be an ast.FunctionDef or ast.AsyncFunctionDef

        Returns:
            List: Returns a List of arguments of the given node.
        """
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            return node.args.args
        return None

    def _format_general_summary(self):
        return self.SUMMARY_LABEL + self.NEW_LINE
    
    def _format_params(self, params):
        if params is None:
            return ""
        label = self.PARAM_LABEL + self.NEW_LINE
        format_params = ""
        for p in params:
            format_params += "- " + p.arg + " () : " + self.TODO_LABEL + self.NEW_LINE
        return label + format_params
    
    def _format_usage_constraints(self):
        return self.CU_LABEL + self.TODO_LABEL + self.NEW_LINE   

    def _format_return_value(self):
        #return_type = self.RETURN_TYPE_LABEL %(self.TODO_LABEL, self.NEW_LINE)
        return_type = self.RETURN_TYPE_LABEL + self.NEW_LINE
        return self.RETURN_LABEL + return_type
    
    def _format_test_examples(self):
        label = self.DOCTEST_LABEL + self.NEW_LINE
        todo = self.TODO_LABEL + self.NEW_LINE
        return label + todo
        
    def get_template(self, node:ast.AST):
        return self.DOCSTRING_SYMBOL + \
               self._format_general_summary() + self.NEW_LINE + \
               self._format_params(self.get_parameters(node))  + \
               self._format_return_value() + \
               self._format_usage_constraints() + \
               self._format_test_examples() + \
               self.DOCSTRING_SYMBOL + self.NEW_LINE

class MinimalistDocTemplate(DefaultDocTemplate):
    """
    The minimalist docstring template don't includes the parameters of a node.
    It overrides the get_parameters() from DefaultDocTemplate class to return an empty list.
    """
    
    # overrided
    def get_parameters(self, node:ast.AST):
        return [] if not node else super().get_parameters(node) 
    
