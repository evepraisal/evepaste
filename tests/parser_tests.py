from evepaste.testing.tables.cargo_scan import CARGO_SCAN_TABLE
from evepaste.testing.tables.human_list import HUMAN_LIST_TABLE
from evepaste.testing.tables.fitting import FITTING_TABLE
from evepaste.testing.tables.eft import EFT_TABLE
from evepaste.testing.tables.dscan import DSCAN_TABLE
from evepaste.testing.tables.loot_history import LOOT_HISTORY_TABLE
from evepaste.testing.tables.contract import CONTRACT_TABLE
from evepaste.testing.tables.assets import ASSET_TABLE
from evepaste.testing.tables.bill_of_materials import BOM_TABLE
from evepaste.testing.tables.manufacturing import MANUFACTURING_TABLE

import inspect
import pprint


class TableChecker(object):
    """ This actually runs one named table test """
    def __init__(self, funct, name):
        self.funct = funct
        self.description = name

    def __call__(self, input_str, expected):
        if inspect.isclass(expected) and issubclass(expected, Exception):
            try:
                self.funct(input_str)
            except expected:
                pass
            else:
                raise AssertionError('Exception %s not raised' % expected)
        else:
            result = self.funct(input_str)
            assert result == expected, '''Unexpected result.
Expected: %s
Actual: %s''' % (pprint.pformat(expected), pprint.pformat(result))


def test_generator():
    for table in [CARGO_SCAN_TABLE,
                  HUMAN_LIST_TABLE,
                  FITTING_TABLE,
                  EFT_TABLE,
                  DSCAN_TABLE,
                  LOOT_HISTORY_TABLE,
                  CONTRACT_TABLE,
                  ASSET_TABLE,
                  BOM_TABLE,
                  MANUFACTURING_TABLE]:
        for i, (input_str, expected) in enumerate(table.tests):
            name = ('test_%s[%s]' % (str(table.funct.__name__), i))
            checker = TableChecker(table.funct, name)
            yield checker, input_str, expected
