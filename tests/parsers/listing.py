"""
tests.parsers.cargo_scan
~~~~~~~~~~~~~~~~~~~~~~~~
Cargo Scan table tests

"""
from evepaste import parse_listing
from tests import TableTestGroup


LISTING_TABLE = TableTestGroup(parse_listing)
LISTING_TABLE.add_test('1 Minmatar Shuttle\n2 Gallente Shuttle',
                       ([{'name': 'Minmatar Shuttle', 'quantity': 1},
                         {'name': 'Gallente Shuttle', 'quantity': 2}], []))
LISTING_TABLE.add_test('\n\n1 Minmatar Shuttle',
                       ([{'name': 'Minmatar Shuttle', 'quantity': 1}], []))
LISTING_TABLE.add_test('10 Minmatar Shuttle\n2 Gallente Shuttle',
                       ([{'name': 'Minmatar Shuttle', 'quantity': 10},
                         {'name': 'Gallente Shuttle', 'quantity': 2}], []))
LISTING_TABLE.add_test('Minmatar Shuttle',
                       ([{'name': 'Minmatar Shuttle', 'quantity': 1}], []))
LISTING_TABLE.add_test('10x Minmatar Shuttle',
                       ([{'name': 'Minmatar Shuttle', 'quantity': 10}], []))
LISTING_TABLE.add_test('Minmatar Shuttle x 10',
                       ([{'name': 'Minmatar Shuttle', 'quantity': 10}], []))

LISTING_TABLE.add_test('10 200mm Afterburner',
                       ([{'name': '200mm Afterburner',
                          'quantity': 10}], []))
