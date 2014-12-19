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
# Test large quantities
LISTING_TABLE.add_test("9'584'701 x Tritanium",
                       ([{'name': 'Tritanium', 'quantity': 9584701}], []))
LISTING_TABLE.add_test(
    '''9'584'701 x Tritanium
2'036'800 x Pyerite
546'300 x Mexallon
149'580 x Isogen
32'410 x Nocxium
7'230 x Zydrine
3'010 x Megacyte''',
    ([
        {'name': u'Isogen',    'quantity':  149580},
        {'name': u'Megacyte',  'quantity':    3010},
        {'name': u'Mexallon',  'quantity':  546300},
        {'name': u'Nocxium',   'quantity':   32410},
        {'name': u'Pyerite',   'quantity': 2036800},
        {'name': u'Tritanium', 'quantity': 9584701},
        {'name': u'Zydrine',   'quantity':    7230},
    ], []))
LISTING_TABLE.add_test("Minmatar Shuttle x 12'000",
                       ([{'name': 'Minmatar Shuttle', 'quantity': 12000}], []))
