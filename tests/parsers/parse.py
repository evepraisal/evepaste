"""
tests.parsers.parse
~~~~~~~~~~~~~~~~~~~
Parse table tests

"""
from evepaste import parse, Unparsable
from tests import TableTestGroup


PARSE_TABLE = TableTestGroup(parse)
PARSE_TABLE.add_test('''rifter
\t\t\t\t\t\t\t\t\t\t''', {'bad_lines': ['\t\t\t\t\t\t\t\t\t\t'],
                          'type': 'listing',
                          'result': [{'name': 'rifter', 'quantity': 1}]})
PARSE_TABLE.add_test('', Unparsable)
