"""
tests.parsers.assets
~~~~~~~~~~~~~~~~~~~~
Asset list table tests

"""
from evepaste import parse_assets
from tests import TableTestGroup


ASSET_TABLE = TableTestGroup(parse_assets)
ASSET_TABLE.add_test('Hurricane\t1\tCombat Battlecruiser\t\t\t15,000 m3',
                     ([{'category': '',
                        'slot': None,
                        'group': 'Combat Battlecruiser',
                        'name': 'Hurricane',
                        'volume': '15,000 m3',
                        'size': '',
                        'tech_level': None,
                        'meta_level': None,
                        'quantity': 1}], []))
ASSET_TABLE.add_test('''
720mm Gallium Cannon\t1\tProjectile Weapon\tMedium\tHigh\t10 m3
Damage Control II\t1\tDamage Control\t\tLow\t5 m3
Experimental 10MN Microwarpdrive I\t1\tPropulsion Module\t\tMedium\t10 m3''',
                     ([{'category': 'Medium',
                        'slot': 'High',
                        'group': 'Projectile Weapon',
                        'name': '720mm Gallium Cannon',
                        'volume': '10 m3',
                        'size': None,
                        'tech_level': None,
                        'meta_level': None,
                        'quantity': 1},
                       {'category': '',
                        'slot': 'Low',
                        'group': 'Damage Control',
                        'name': 'Damage Control II',
                        'volume': '5 m3',
                        'size': None,
                        'tech_level': None,
                        'meta_level': None,
                        'quantity': 1},
                       {'category': '',
                        'slot': None,
                        'group': 'Propulsion Module',
                        'name': 'Experimental 10MN Microwarpdrive I',
                        'volume': '10 m3',
                        'size': 'Medium',
                        'tech_level': None,
                        'meta_level': None,
                        'quantity': 1}], []))
ASSET_TABLE.add_test('''
200mm AutoCannon I\t1\tProjectile Weapon\tModule\tSmall\tHigh\t5 m3\t\t1
10MN Afterburner II\t1\tPropulsion Module\tModule\t\tMedium\t5 m3\t5\t2
Warrior II\t9''',
                     ([{'category': 'Module',
                        'slot': 'High',
                        'group': 'Projectile Weapon',
                        'name': '200mm AutoCannon I',
                        'volume': '5 m3',
                        'size': 'Small',
                        'tech_level': '1',
                        'meta_level': '',
                        'quantity': 1},
                       {'category': 'Module',
                        'slot': 'Medium',
                        'group': 'Propulsion Module',
                        'name': '10MN Afterburner II',
                        'volume': '5 m3',
                        'size': '',
                        'tech_level': '2',
                        'meta_level': '5',
                        'quantity': 1},
                       {'category': None,
                        'slot': None,
                        'group': None,
                        'name': 'Warrior II',
                        'volume': None,
                        'size': None,
                        'tech_level': None,
                        'meta_level': None,
                        'quantity': 9}], []))
ASSET_TABLE.add_test('hurricane\t20', ([{'category': None,
                                         'slot': None,
                                         'group': None,
                                         'name': 'hurricane',
                                         'volume': None,
                                         'size': None,
                                         'tech_level': None,
                                         'meta_level': None,
                                         'quantity': 20}], []))
ASSET_TABLE.add_test('''
Sleeper Data Library\t1.080\tSleeper Components\t\t\t10.80 m3
''', ([{'category': '',
        'group': 'Sleeper Components',
        'meta_level': None,
        'name': 'Sleeper Data Library',
        'quantity': 1080,
        'size': '',
        'slot': None,
        'tech_level': None,
        'volume': '10.80 m3'}], []))
ASSET_TABLE.add_test(u'''
Sleeper Data Library\t1\xc2\xa0080\tSleeper Components\t\t\t10.80 m3
''', ([{'category': '',
        'group': 'Sleeper Components',
        'meta_level': None,
        'name': 'Sleeper Data Library',
        'quantity': 1080,
        'size': '',
        'slot': None,
        'tech_level': None,
        'volume': '10.80 m3'}], []))
ASSET_TABLE.add_test('''
Sleeper Data Library\t1,080\tSleeper Components\t\t\t10.80 m3
''', ([{'category': '',
        'group': 'Sleeper Components',
        'meta_level': None,
        'name': 'Sleeper Data Library',
        'quantity': 1080,
        'size': '',
        'slot': None,
        'tech_level': None,
        'volume': '10.80 m3'}], []))
ASSET_TABLE.add_test('''
Amarr Dreadnought\t1\tSpaceship Command\tSkill\t\t\t0.01 m3\t\t
''', ([{'category': 'Skill',
        'slot': '',
        'group': 'Spaceship Command',
        'name': 'Amarr Dreadnought',
        'volume': '0.01 m3',
        'size': '',
        'tech_level': '',
        'meta_level': '',
        'quantity': 1}], []))
ASSET_TABLE.add_test('''
Quafe Zero\t12\tBooster\tImplant\t\t1 \t12 m3\t\t
''', ([{'category': 'Implant',
        'slot': '1 ',
        'group': 'Booster',
        'name': 'Quafe Zero',
        'volume': '12 m3',
        'size': '',
        'tech_level': '',
        'meta_level': '',
        'quantity': 12}], []))
ASSET_TABLE.add_test(
    u"Antimatter Charge M\t100\xc2\xa0000\tHybrid Charge\tMedium\t\t"
    u"1\xc2\xa0250 m3",
    ([{'category': 'Medium',
     'group': 'Hybrid Charge',
     'meta_level': None,
     'name': 'Antimatter Charge M',
     'quantity': 100000,
     'size': '',
     'slot': None,
     'tech_level': None,
     'volume': '1250 m3'}], []))
