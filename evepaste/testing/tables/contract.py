"""
evepaste.testing.tables.contract
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Contract table tests

"""
from evepaste import parse_contract
from evepaste.testing import TableTestGroup


CONTRACT_TABLE = TableTestGroup(parse_contract)
CONTRACT_TABLE.add_test('Rokh\t1\tBattleship\tShip\t',
                        ([{'name': 'Rokh',
                           'quantity': 1,
                           'type': 'Battleship',
                           'category': 'Ship',
                           'info': '',
                           'fitted': False}], []))
CONTRACT_TABLE.add_test('''Rokh\t1\tBattleship\tShip\t
 Large Core Defense Field Extender I\t1\tRig Shield\tModule\tFitted''',
                        ([{'name': 'Rokh',
                           'quantity': 1,
                           'type': 'Battleship',
                           'category': 'Ship',
                           'info': '',
                           'fitted': False},
                          {'name': 'Large Core Defense Field Extender I',
                           'quantity': 1,
                           'type': 'Rig Shield',
                           'category': 'Module',
                           'info': 'Fitted',
                           'fitted': True}], []))
CONTRACT_TABLE.add_test('''Rokh\t1\tBattleship\tShip\t
 Large Core Defense Field Extender I\t1\tRig Shield\tModule\tFitted
 Scorch M\t1\tAdvanced Pulse Laser Crystal\tCharge\tFitted 72% damaged
 Scorch L\t2\tAdvanced Pulse Laser Crystal\tCharge\t 1% damaged
 ''',
                        ([{'category': 'Ship',
                           'info': '',
                           'name': 'Rokh',
                           'type': 'Battleship',
                           'fitted': False,
                           'quantity': 1},
                          {'category': 'Module',
                           'info': 'Fitted',
                           'name': 'Large Core Defense Field Extender I',
                           'type': 'Rig Shield',
                           'fitted': True,
                           'quantity': 1},
                          {'category': 'Charge',
                           'info': 'Fitted 72% damaged',
                           'name': 'Scorch M',
                           'type': 'Advanced Pulse Laser Crystal',
                           'fitted': True,
                           'quantity': 1},
                          {'category': 'Charge',
                           'info': ' 1% damaged',
                           'name': 'Scorch L',
                           'type': 'Advanced Pulse Laser Crystal',
                           'fitted': False,
                           'quantity': 2}], []))
CONTRACT_TABLE.add_test('Rokh', ([], ['Rokh']))
