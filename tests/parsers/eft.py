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
[empty high slot]''', ({
    'ship': 'Rifter',
    'name': 'Fleet Tackle',
    'modules': [{'name': '200mm AutoCannon I', 'ammo': 'EMP S'},
                {'name': '200mm AutoCannon I', 'ammo': 'EMP S'},
                {'name': '200mm AutoCannon I', 'ammo': 'EMP S'},
                {'name': 'Nanofiber Internal Structure I'},
                {'name': 'Nanofiber Internal Structure I'},
                {'name': 'Overdrive Injector System I'},
                {'name': 'Stasis Webifier I'},
                {'name': 'Warp Disruptor I'},
                {'name': '1MN Microwarpdrive I'}]
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
                {'name': 'Heat Sink II'},
                {'name': 'Heat Sink II'},
                {'name': 'Heat Sink II'},
                {'name': 'Tracking Enhancer II'},
                {'name': 'Tracking Enhancer II'},
                {'name': 'Reactor Control Unit II'},
                {'name': 'Beta Reactor Control: Reaction Control I'},
                {'name': '100MN Microwarpdrive I'},
                {'name': 'F-90 Positional Sensor Subroutines'}],
    'ship': 'Apocalypse',
    'name': "Pimpin' Sniper Fit"}, []))
EFT_TABLE.add_test('[Rifter,test]',
                   ({'modules': [], 'name': 'test', 'ship': 'Rifter'}, []))
EFT_TABLE.add_test('', Unparsable)
EFT_TABLE.add_test('[test]', Unparsable)
