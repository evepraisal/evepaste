"""
eve_paste.testing
~~~~~~~~~~~~~~~~~
Utilities and re-usable helper functions for evepaste

"""


class TableTestGroup(object):
    def __init__(self, funct):
        self.funct = funct
        self.tests = []

    def add_test(self, input_str, expected):
        self.tests.append((input_str, expected))
