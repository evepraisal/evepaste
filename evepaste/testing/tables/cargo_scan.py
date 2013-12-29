from evepaste import parse_cargo_scan
from evepaste.testing import TableTestGroup


CARGO_SCAN_TABLE = TableTestGroup(parse_cargo_scan)
CARGO_SCAN_TABLE.add_test('1 Minmatar Shuttle\n2 Gallente Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 1},
                            {'name': 'Gallente Shuttle', 'quantity': 2}], []))

CARGO_SCAN_TABLE.add_test('Minmatar Shuttle', ([], ['Minmatar Shuttle']))
CARGO_SCAN_TABLE.add_test('\n\n1 Minmatar Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 1}], []))
