"""
evepaste.testing.tables.parse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Parse table tests

"""
from evepaste import parse, Unparsable
from evepaste.testing import TableTestGroup


PARSE_TABLE = TableTestGroup(parse)
PARSE_TABLE.add_test('', Unparsable)
