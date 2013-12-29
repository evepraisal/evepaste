"""
evepaste.testing
~~~~~~~~~~~~~~~~
Utilities and re-usable helper functions for evepaste

"""


class TableTestGroup(object):
    """
    A table test group - A collection of tests to run against one callable.

    :param funct: A callable that will be called with each test
    """
    def __init__(self, funct):
        self.funct = funct
        self.tests = []

    def add_test(self, input_str, expected):
        """
        Add a test to the collection

        :param str input_str: To be used as the only positional argument
        :param expected: The expected output of the function called with
                         input_str.
        """
        self.tests.append((input_str, expected))
