from evepaste import parse
from tests import parsers, TableChecker


def test_generator():
    # Perform each table test with their associated callable
    for table in [parsers.LISTING_TABLE,
                  parsers.FITTING_TABLE,
                  parsers.EFT_TABLE,
                  parsers.DSCAN_TABLE,
                  parsers.LOOT_HISTORY_TABLE,
                  parsers.CONTRACT_TABLE,
                  parsers.ASSET_TABLE,
                  parsers.BOM_TABLE,
                  parsers.VIEW_CONTENTS_TABLE,
                  parsers.PARSE_TABLE]:
        for i, (input_str, expected) in enumerate(table.tests):
            name = ('test_%s[%s]' % (str(table.funct.__name__), i))
            checker = TableChecker(table.funct, name)
            yield checker, input_str, expected

    # Perform each table test with parse() instead of the associated callable
    for table in [parsers.LISTING_TABLE,
                  parsers.FITTING_TABLE,
                  parsers.EFT_TABLE,
                  parsers.DSCAN_TABLE,
                  parsers.LOOT_HISTORY_TABLE,
                  parsers.CONTRACT_TABLE,
                  parsers.ASSET_TABLE,
                  parsers.BOM_TABLE,
                  parsers.VIEW_CONTENTS_TABLE]:
        for i, (input_str, expected) in enumerate(table.tests):
            if isinstance(expected, tuple) and not expected[1]:
                name = ('test_parse(%s)[%s]' % (str(table.funct.__name__), i))
                checker = TableChecker(parse, name)
                result, bad_lines = expected
                _type = table.funct.__name__.split('_', 1)[1]
                yield checker, input_str, (_type, result, bad_lines)
