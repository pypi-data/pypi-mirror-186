# Auteur : Esteban COLLARD, Nordine EL AMMARI

from .Test import Test

class PassedTest(Test):
    def __init__(self, filename, node, tested_line, expected_result, lineno):
        super().__init__(filename, node, tested_line, expected_result, lineno)

    def get_tag(self):
        return "green"
    
    def __str__(self):
        report = "Test OK for: %s " % (self.tested_line)
        return report
