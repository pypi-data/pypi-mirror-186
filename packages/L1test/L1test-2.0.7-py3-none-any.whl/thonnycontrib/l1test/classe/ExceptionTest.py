# Auteur : Esteban COLLARD, Nordine EL AMMARI

from .Test import Test

class ExceptionTest(Test):
    def __init__(self, filename, node, tested_line, expected_result, lineno, exception):
        super().__init__(filename, node, tested_line, expected_result, lineno)
        self.exception = exception

    def get_exception(self):
        return self.exception

    def get_tag(self):
        return "red"
    
    def __str__(self):
        report = "- Test raises exception for `%s`" % (self.tested_line)
        return report

    def get_detail_failure(self):
        return self.exception
