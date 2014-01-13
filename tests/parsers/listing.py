"""
tests.parsers.listing
~~~~~~~~~~~~~~~~~~~~~~~~
Listing table tests

"""
from evepaste import parse_listing
from tests import TableTestGroup


LISTING_TABLE = TableTestGroup(parse_listing)
LISTING_TABLE.add_test('Minmatar Shuttle',
                       ([{'name': 'Minmatar Shuttle', 'quantity': 1}], []))
LISTING_TABLE.add_test('10x Minmatar Shuttle',
                       ([{'name': 'Minmatar Shuttle', 'quantity': 10}], []))
LISTING_TABLE.add_test('Minmatar Shuttle x 10',
                       ([{'name': 'Minmatar Shuttle', 'quantity': 10}], []))
LISTING_TABLE.add_test(', Heavy Assault Missile Launcher II,',
                       ([{'name': 'Heavy Assault Missile Launcher II,',
                          'quantity': 1}], []))
LISTING_TABLE.add_test('Heavy Assault Missile Launcher II 10',
                       ([{'name': 'Heavy Assault Missile Launcher II',
                          'quantity': 10}], []))
