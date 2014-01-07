"""
tests.parsers.contract
~~~~~~~~~~~~~~~~~~~~~~
Contract table tests

"""
from evepaste import parse_contract
from tests import TableTestGroup


CONTRACT_TABLE = TableTestGroup(parse_contract)
CONTRACT_TABLE.add_test('Rokh\t1\tBattleship\tShip\t',
                        ([{'name': 'Rokh',
                           'quantity': 1,
                           'type': 'Battleship',
                           'category': 'Ship',
                           'details': '',
                           'fitted': False}], []))
CONTRACT_TABLE.add_test('''Rokh\t1\tBattleship\tShip\t
 Large Core Defense Field Extender I\t1\tRig Shield\tModule\tFitted''',
                        ([{'category': 'Module',
                           'details': 'Fitted',
                           'fitted': True,
                           'name': 'Large Core Defense Field Extender I',
                           'quantity': 1,
                           'type': 'Rig Shield'},
                          {'category': 'Ship',
                           'details': '',
                           'fitted': False,
                           'name': 'Rokh',
                           'quantity': 1,
                           'type': 'Battleship'}], []))
CONTRACT_TABLE.add_test('''Rokh\t1\tBattleship\tShip\t
 Large Core Defense Field Extender I\t1\tRig Shield\tModule\tFitted
 Scorch M\t1\tAdvanced Pulse Laser Crystal\tCharge\tFitted 72% damaged
 Scorch L\t2\tAdvanced Pulse Laser Crystal\tCharge\t 1% damaged''',
                        ([{'category': 'Module',
                           'details': 'Fitted',
                           'fitted': True,
                           'name': 'Large Core Defense Field Extender I',
                           'quantity': 1,
                           'type': 'Rig Shield'},
                          {'category': 'Ship',
                           'details': '',
                           'fitted': False,
                           'name': 'Rokh',
                           'quantity': 1,
                           'type': 'Battleship'},
                          {'category': 'Charge',
                           'details': ' 1% damaged',
                           'fitted': False,
                           'name': 'Scorch L',
                           'quantity': 2,
                           'type': 'Advanced Pulse Laser Crystal'},
                          {'category': 'Charge',
                           'details': 'Fitted 72% damaged',
                           'fitted': True,
                           'name': 'Scorch M',
                           'quantity': 1,
                           'type': 'Advanced Pulse Laser Crystal'}], []))
CONTRACT_TABLE.add_test('''
Armageddon Blueprint\t1\tBattleship Blueprint\tBlueprint\tBLUEPRINT COPY - \
Runs: 9 - Material Level: 29 - Productivity Level: 0
''', ([{'category': 'Blueprint',
        'fitted': False,
        'details': 'BLUEPRINT COPY - Runs: 9 - '
        'Material Level: 29 - Productivity Level: 0',
        'name': 'Armageddon Blueprint',
        'quantity': 1,
        'type': 'Battleship Blueprint'}], []))
CONTRACT_TABLE.add_test('425mm Railgun I\t2000\tHybrid Weapon',
                        ([{'name': '425mm Railgun I',
                           'type': 'Hybrid Weapon',
                           'quantity': 2000}], []))
CONTRACT_TABLE.add_test('Rokh', ([], ['Rokh']))
