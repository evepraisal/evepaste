from evepaste.testing.tables.cargo_scan import CARGO_SCAN_TABLE
from evepaste.testing.tables.human_list import HUMAN_LIST_TABLE
from evepaste.testing.tables.eft import EFT_TABLE
from evepaste.testing.tables.dscan import DSCAN_TABLE

import inspect


def check_table(funct, input_str, expected):
    if inspect.isclass(expected) and issubclass(expected, Exception):
        try:
            funct(input_str)
        except expected:
            pass
        else:
            raise AssertionError('Exception %s not raised' % expected)
    else:
        result = funct(input_str)
        assert result == expected, '''Unexpected result.
Expected: %s
Actual: %s''' % (expected, result)


def test_generator():
    for table in [CARGO_SCAN_TABLE,
                  HUMAN_LIST_TABLE,
                  EFT_TABLE,
                  DSCAN_TABLE]:
        for i, (input_str, expected) in enumerate(table.tests):
            check_table.description = ('TableTest: %s[%s]'
                                       % (str(table.funct.__name__), i))
            yield check_table, table.funct, input_str, expected
