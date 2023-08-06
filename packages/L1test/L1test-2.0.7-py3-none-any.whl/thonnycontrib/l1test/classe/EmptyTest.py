from ..utils import create_node_representation
from .Test import Test

class EmptyTest(Test):
    def __init__(self, filename, node, lineno):
        super().__init__(filename, node, None, None, lineno)

    def get_tag(self):
        return "orange"
    
    def __str__(self):
        empty_node = create_node_representation(self.node)
        return "No test detected for: %s \n\n" % (empty_node)
