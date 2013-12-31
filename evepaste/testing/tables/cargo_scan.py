"""
evepaste.testing.tables.cargo_scan
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cargo Scan table tests

"""
from evepaste import parse_cargo_scan
from evepaste.testing import TableTestGroup


CARGO_SCAN_TABLE = TableTestGroup(parse_cargo_scan)
CARGO_SCAN_TABLE.add_test('1 Minmatar Shuttle\n2 Gallente Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 1},
                            {'name': 'Gallente Shuttle', 'quantity': 2}], []))
CARGO_SCAN_TABLE.add_test('\n\n1 Minmatar Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 1}], []))
CARGO_SCAN_TABLE.add_test('10 Minmatar Shuttle\n2 Gallente Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 10},
                            {'name': 'Gallente Shuttle', 'quantity': 2}], []))
CARGO_SCAN_TABLE.add_test('Minmatar Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 1}], []))
CARGO_SCAN_TABLE.add_test('10x Minmatar Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 10}], []))
CARGO_SCAN_TABLE.add_test('10xMinmatar Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 10}], []))
CARGO_SCAN_TABLE.add_test('Minmatar Shuttle x 10',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 10}], []))
