"""
tests
~~~~~
Tests and test helpers for evepaste

"""

import inspect
import unittest


class TableChecker(unittest.TestCase):
    """ This actually runs one named table test """
    def __init__(self, funct, name):
        unittest.TestCase.__init__(self, 'run')
        self.funct = funct
        self.description = name

    def run(self, input_str, expected):
        self.maxDiff = 1000000
        if inspect.isclass(expected) and issubclass(expected, Exception):
            self.assertRaises(expected, self.funct, input_str)
        else:
            result = self.funct(input_str)
            self.assertEqual(result, expected)


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
