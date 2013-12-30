"""
evepaste.testing.tables.manufacturing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Manufacturing table tests

"""
from evepaste import parse_manufacturing
from evepaste.testing import TableTestGroup


MANUFACTURING_TABLE = TableTestGroup(parse_manufacturing)
MANUFACTURING_TABLE.add_test('Rokh\t1\tBattleship\tShip\tBlueprint Copy',
                             ([{'name': 'Rokh',
                                'quantity': 1,
                                'type': 'Battleship',
                                'category': 'Ship',
                                'info': 'Blueprint Copy'}], []))
MANUFACTURING_TABLE.add_test('''Rokh\t1\tBattleship\tShip\tBlueprint Copy
Rokh\t1\tBattleship\tShip\tBlueprint Copy''',
                             ([{'name': 'Rokh',
                                'quantity': 1,
                                'type': 'Battleship',
                                'category': 'Ship',
                                'info': 'Blueprint Copy'},
                               {'name': 'Rokh',
                                'quantity': 1,
                                'type': 'Battleship',
                                'category': 'Ship',
                                'info': 'Blueprint Copy'}], []))
