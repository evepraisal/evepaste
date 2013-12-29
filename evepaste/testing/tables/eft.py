from evepaste import parse_eft
from evepaste.exceptions import Unparsable
from evepaste.testing import TableTestGroup

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
    'modules': ['Nanofiber Internal Structure I',
                'Nanofiber Internal Structure I',
                'Overdrive Injector System I',
                'Stasis Webifier I',
                'Warp Disruptor I',
                '1MN Microwarpdrive I',
                '200mm AutoCannon I',
                '200mm AutoCannon I',
                '200mm AutoCannon I']
    }, []))
EFT_TABLE.add_test('', Unparsable)
EFT_TABLE.add_test('[test]', Unparsable)
EFT_TABLE.add_test('[Rifter,test]',
                   ({'modules': [], 'name': 'test', 'ship': 'Rifter'}, []))
