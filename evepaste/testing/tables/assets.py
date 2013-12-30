"""
evepaste.testing.tables.assets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Asset list table tests

"""
from evepaste import parse_asset_list
from evepaste.testing import TableTestGroup


ASSET_TABLE = TableTestGroup(parse_asset_list)
ASSET_TABLE.add_test('Hurricane\t1\tCombat Battlecruiser\t\t\t15,000 m3',
                     ([{'name': 'Hurricane',
                        'quantity': 1,
                        'group': 'Combat Battlecruiser',
                        'size': '',
                        'slot': '',
                        'volume': '15,000 m3'}], []))
ASSET_TABLE.add_test('''
720mm Gallium Cannon\t1\tProjectile Weapon\tMedium\tHigh\t10 m3
Damage Control II\t1\tDamage Control\t\tLow\t5 m3
Experimental 10MN Microwarpdrive I\t1\tPropulsion Module\t\tMedium\t10 m3''',
                     ([{'slot': 'High',
                        'group': 'Projectile Weapon',
                        'name': '720mm Gallium Cannon',
                        'volume': '10 m3',
                        'quantity': 1,
                        'size': 'Medium'},
                       {'slot': 'Low',
                        'group': 'Damage Control',
                        'name': 'Damage Control II',
                        'volume': '5 m3',
                        'quantity': 1,
                        'size': ''},
                       {'slot': 'Medium',
                        'group': 'Propulsion Module',
                        'name': 'Experimental 10MN Microwarpdrive I',
                        'volume': '10 m3',
                        'quantity': 1,
                        'size': ''}], []))
ASSET_TABLE.add_test('hurricane', ([], ['hurricane']))
ASSET_TABLE.add_test('', ([], []))
