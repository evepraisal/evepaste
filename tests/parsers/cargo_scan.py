"""
tests.parsers.cargo_scan
~~~~~~~~~~~~~~~~~~~~~~~~
Cargo Scan table tests

"""
from evepaste import parse_cargo_scan
from tests import TableTestGroup


CARGO_SCAN_TABLE = TableTestGroup(parse_cargo_scan)
CARGO_SCAN_TABLE.add_test('''1 Minmatar Shuttle
2 Gallente Shuttle''', ([{'name': 'Gallente Shuttle', 'quantity': 2},
                         {'name': 'Minmatar Shuttle', 'quantity': 1}], []))
CARGO_SCAN_TABLE.add_test('\n\n1 Minmatar Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 1}], []))
CARGO_SCAN_TABLE.add_test('10 Minmatar Shuttle\n2 Gallente Shuttle',
                          ([{'name': 'Gallente Shuttle', 'quantity': 2},
                            {'name': 'Minmatar Shuttle', 'quantity': 10}], []))
CARGO_SCAN_TABLE.add_test(
    '10 200mm Afterburner',
    ([{'name': '200mm Afterburner', 'quantity': 10}], []))
CARGO_SCAN_TABLE.add_test(
    '10 Plagioclase Mining Crystal I Blueprint (Original)',
    ([{'name': 'Plagioclase Mining Crystal I Blueprint',
       'quantity': 10,
       'details': 'BLUEPRINT ORIGINAL'}], []))
CARGO_SCAN_TABLE.add_test('10 Plagioclase Mining Crystal I Blueprint (Copy)',
                          ([{'name': 'Plagioclase Mining Crystal I Blueprint',
                             'quantity': 10,
                             'details': 'BLUEPRINT COPY'}], []))
