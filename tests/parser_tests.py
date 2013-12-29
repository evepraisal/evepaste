import unittest
import inspect

from evepaste import parse_cargo_scan, parse_human_listing, parse_eft
from evepaste.exceptions import Unparsable


CARGO_SCAN_TABLE = [
    ('1 Minmatar Shuttle\n2 Gallente Shuttle',
     [{'name': 'Minmatar Shuttle', 'quantity': 1},
      {'name': 'Gallente Shuttle', 'quantity': 2}]),
    ('Minmatar Shuttle', []),
    ('\n\n1 Minmatar Shuttle', [{'name': 'Minmatar Shuttle', 'quantity': 1}]),
]

HUMAN_LIST_TABLE = [
    ('1 Minmatar Shuttle\n2 Gallente Shuttle',
     [{'name': 'Minmatar Shuttle', 'quantity': 1},
      {'name': 'Gallente Shuttle', 'quantity': 2}]),
    ('Minmatar Shuttle', [{'name': 'Minmatar Shuttle', 'quantity': 1}]),
    ('1x Minmatar Shuttle', [{'name': 'Minmatar Shuttle', 'quantity': 1}]),
    ('1xMinmatar Shuttle', [{'name': 'Minmatar Shuttle', 'quantity': 1}]),
]

EFT_TABLE = [
    ('''[Rifter, Fleet Tackle]
Nanofiber Internal Structure I
Nanofiber Internal Structure I
Overdrive Injector System I

Stasis Webifier I
Warp Disruptor I
1MN Microwarpdrive I

200mm AutoCannon I, EMP S
200mm AutoCannon I, EMP S
200mm AutoCannon I, EMP S
[empty high slot]''',
     {'ship': 'Rifter',
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
      }),
    ('', Unparsable),
    ('[test]', Unparsable),
    ('[Rifter,test]', {'modules': [], 'name': 'test', 'ship': 'Rifter'}),
]


class TestParsers(unittest.TestCase):

    def _run_table_tests(self, f, table):
        for input_str, expected in table:
            if inspect.isclass(expected) and issubclass(expected, Exception):
                self.assertRaises(expected, f, input_str)
            else:
                result = f(input_str)
                self.assertEquals(result, expected)

    def test_cargo_scan(self):
        self._run_table_tests(parse_cargo_scan, CARGO_SCAN_TABLE)

    def test_parse_human_listing(self):
        self._run_table_tests(parse_human_listing, HUMAN_LIST_TABLE)

    def test_parse_eft(self):
        self._run_table_tests(parse_eft, EFT_TABLE)
