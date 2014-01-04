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
''', ({
    'ship': 'Rifter',
    'name': 'Fleet Tackle',
    'modules': [{'name': '200mm AutoCannon I', 'ammo': 'EMP S'},
                {'name': '200mm AutoCannon I', 'ammo': 'EMP S'},
                {'name': '200mm AutoCannon I', 'ammo': 'EMP S'},
                {'name': 'Garde I', 'quantity': 5},
                {'name': 'Nanofiber Internal Structure I', 'quantity': 1},
                {'name': 'Nanofiber Internal Structure I', 'quantity': 1},
                {'name': 'Overdrive Injector System I', 'quantity': 1},
                {'name': 'Stasis Webifier I', 'quantity': 1},
                {'name': 'Warp Disruptor I', 'quantity': 1},
                {'name': '1MN Microwarpdrive I', 'quantity': 1}]
    }, []))
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
Tachyon Beam Laser II, Aurora L''', ({
    'modules': [{'name': 'Sensor Booster II',
                 'ammo': 'Targeting Range Script'},
                {'name': 'Sensor Booster II',
                 'ammo': 'Targeting Range Script'},
                {'name': 'Tachyon Beam Laser II', 'ammo': 'Aurora L'},
                {'name': 'Tachyon Beam Laser II', 'ammo': 'Aurora L'},
                {'name': 'Tachyon Beam Laser II', 'ammo': 'Aurora L'},
                {'name': 'Tachyon Beam Laser II', 'ammo': 'Aurora L'},
                {'name': 'Tachyon Beam Laser II', 'ammo': 'Aurora L'},
                {'name': 'Tachyon Beam Laser II', 'ammo': 'Aurora L'},
                {'name': 'Tachyon Beam Laser II', 'ammo': 'Aurora L'},
                {'name': 'Tachyon Beam Laser II', 'ammo': 'Aurora L'},
                {'name': 'Heat Sink II', 'quantity': 1},
                {'name': 'Heat Sink II', 'quantity': 1},
                {'name': 'Heat Sink II', 'quantity': 1},
                {'name': 'Tracking Enhancer II', 'quantity': 1},
                {'name': 'Tracking Enhancer II', 'quantity': 1},
                {'name': 'Reactor Control Unit II', 'quantity': 1},
                {'name': 'Beta Reactor Control: Reaction Control I',
                 'quantity': 1},
                {'name': '100MN Microwarpdrive I', 'quantity': 1},
                {'name': 'F-90 Positional Sensor Subroutines', 'quantity': 1}],
    'ship': 'Apocalypse',
    'name': "Pimpin' Sniper Fit"}, []))
EFT_TABLE.add_test('[Rifter,test]',
                   ({'modules': [], 'name': 'test', 'ship': 'Rifter'}, []))
EFT_TABLE.add_test('', Unparsable)
EFT_TABLE.add_test('[test]', Unparsable)
