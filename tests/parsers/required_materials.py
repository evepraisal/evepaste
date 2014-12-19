"""
tests.parsers.required_materials
~~~~~~~~~~~~~~~~~~~~~~~~
Blueprint Info required materials table tests

"""
from evepaste import parse_listing
from tests import TableTestGroup


REQUIRED_MATERIALS_TABLE = TableTestGroup(parse_required_materials)
REQUIRED_MATERIALS_TABLE.addTest('9'584'701 x Tritanium',
    ([{'name': 'Tritanium', 'quantity': 9584701}], []))

REQUIRED_MATERIALS_TABLE.addTest(
    '''9'584'701 x Tritanium
2'036'800 x Pyerite
546'300 x Mexallon
149'580 x Isogen
32'410 x Nocxium
7'230 x Zydrine
3'010 x Megacyte''',
    ([
        {'name': 'Tritanium', 'quantity': 9584701},
        {'name': 'Pyerite',   'quantity': 2036800},
        {'name': 'Mexallon',  'quantity':  546300},
        {'name': 'Isogen',    'quantity':  149580},
        {'name': 'Nocxium',   'quantity':   32410},
        {'name': 'Zydrine',   'quantity':    7230},
        {'name': 'Megacyte',  'quantity':    3010},
    ], []))
