"""
evepaste.testing.tables.contract
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Contract table tests

"""
from evepaste import parse_contract
from evepaste.testing import TableTestGroup


CONTRACT_TABLE = TableTestGroup(parse_contract)
CONTRACT_TABLE.add_test('''Rokh\t1\tBattleship\tShip\t''',
                        ([{'name': 'Rokh',
                           'quantity': 1,
                           'type': 'Battleship',
                           'category': 'Ship',
                           'fitted': False}], []))
CONTRACT_TABLE.add_test('''Rokh\t1\tBattleship\tShip\t
 Large Core Defense Field Extender I\t1\tRig Shield\tModule\tFitted''',
                        ([{'name': 'Rokh',
                           'quantity': 1,
                           'type': 'Battleship',
                           'category': 'Ship',
                           'fitted': False},
                          {'name': 'Large Core Defense Field Extender I',
                           'quantity': 1,
                           'type': 'Rig Shield',
                           'category': 'Module',
                           'fitted': True}], []))
CONTRACT_TABLE.add_test('Rokh', ([], ['Rokh']))
