"""
tests.parsers.parse
~~~~~~~~~~~~~~~~~~~
Parse table tests

"""
from evepaste import parse, Unparsable
from tests import TableTestGroup


PARSE_TABLE = TableTestGroup(parse)
PARSE_TABLE.add_test('''10 rifter
\t\t\t\t\t\t\t\t\t\t''', ('cargo_scan',
                          [{'name': 'rifter', 'quantity': 10}],
                          ['\t\t\t\t\t\t\t\t\t\t']))
PARSE_TABLE.add_test('', Unparsable)
