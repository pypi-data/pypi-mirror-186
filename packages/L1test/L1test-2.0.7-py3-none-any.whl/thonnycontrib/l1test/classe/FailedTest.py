# Auteur : Esteban COLLARD, Nordine EL AMMARI

from .Test import Test

class FailedTest(Test):
    def __init__(self, filename:str, node, tested_line, expected_result, lineno, obtained_result):
        super().__init__(filename, node, tested_line, expected_result, lineno)
        self.obtained_result = obtained_result

    def get_obtained_result(self):
        return self.obtained_result

    def get_tag(self):
        return "red"
    
    def __str__(self):
        report = "Test failed for: %s" % (self.tested_line)
        return report

    def get_detail_failure(self):
        want, got = self.expected_result, self.obtained_result
        if got and want:
            diff = 'Expected: %s, Got: %s' % (want, got)
        elif want:
            diff = 'Expected: %s, Got nothing.' % want
        elif got:
            diff = 'Expected nothing, Got: %s' % got
        else:
            diff = 'Expected nothing, Got nothing.'
        return diff
