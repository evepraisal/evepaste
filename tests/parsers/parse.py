"""
tests.parsers.parse
~~~~~~~~~~~~~~~~~~~
Parse table tests

"""
from evepaste import parse, Unparsable
from tests import TableTestGroup


PARSE_TABLE = TableTestGroup(parse)
PARSE_TABLE.add_test('', Unparsable)
