"""
tests.parsers.eft
~~~~~~~~~~~~~~~~~
EFT table tests

"""
from evepaste import parse_eft
from evepaste.exceptions import Unparsable
from tests import TableTestGroup

EFT_TABLE = TableTestGroup(parse_eft)
EFT_TABLE.add_test('''[Rifter, Fleet Tackle]
Nanofiber Internal Structure I
Nanofiber Internal Structure I
Overdrive Injector System I

Stasis Webifier I
Warp Disruptor I
1MN Microwarpdrive I

200mm AutoCannon I, EMP S
200mm AutoCannon I, EMP S
200mm AutoCannon I, EMP S
[empty high slot]

Garde I x5
''', ({'modules': [{'ammo': 'EMP S', 'name': '200mm AutoCannon I',
                    'quantity': 3},
                   {'name': '1MN Microwarpdrive I', 'quantity': 1},
                   {'name': 'Garde I', 'quantity': 5},
                   {'name': 'Nanofiber Internal Structure I', 'quantity': 2},
                   {'name': 'Overdrive Injector System I', 'quantity': 1},
                   {'name': 'Stasis Webifier I', 'quantity': 1},
                   {'name': 'Warp Disruptor I', 'quantity': 1}],
       'name': 'Fleet Tackle',
       'ship': 'Rifter'}, []))

EFT_TABLE.add_test('''
[Apocalypse, Pimpin' Sniper Fit]
Heat Sink II
Heat Sink II
Heat Sink II
Tracking Enhancer II
Tracking Enhancer II
Reactor Control Unit II
Beta Reactor Control: Reaction Control I

100MN Microwarpdrive I
Sensor Booster II, Targeting Range Script
Sensor Booster II, Targeting Range Script
F-90 Positional Sensor Subroutines

Tachyon Beam Laser II, Aurora L
Tachyon Beam Laser II, Aurora L
Tachyon Beam Laser II, Aurora L
Tachyon Beam Laser II, Aurora L
Tachyon Beam Laser II, Aurora L
Tachyon Beam Laser II, Aurora L
Tachyon Beam Laser II, Aurora L
Tachyon Beam Laser II, Aurora L''', (
    {'modules': [{'ammo': 'Aurora L',
                  'name': 'Tachyon Beam Laser II',
                  'quantity': 8},
                 {'ammo': 'Targeting Range Script',
                  'name': 'Sensor Booster II',
                  'quantity': 2},
                 {'name': '100MN Microwarpdrive I', 'quantity': 1},
                 {'name': 'Beta Reactor Control: Reaction Control I',
                  'quantity': 1},
                 {'name': 'F-90 Positional Sensor Subroutines', 'quantity': 1},
                 {'name': 'Heat Sink II', 'quantity': 3},
                 {'name': 'Reactor Control Unit II', 'quantity': 1},
                 {'name': 'Tracking Enhancer II', 'quantity': 2}],
     'name': "Pimpin' Sniper Fit",
     'ship': 'Apocalypse'}, []))
EFT_TABLE.add_test('[Rifter,test]',
                   ({'modules': [], 'name': 'test', 'ship': 'Rifter'}, []))
EFT_TABLE.add_test('', Unparsable)
EFT_TABLE.add_test('[test]', Unparsable)
