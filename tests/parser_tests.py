import unittest
import inspect

from evepaste import (
    parse_cargo_scan, parse_human_listing, parse_eft, parse_dscan)
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

DSCAN_TABLE = [
    ('''+\tNoctis\t3,225 m
+\tThrasher\t12 km
some dude's Stabber Fleet Issue\tStabber Fleet Issue\t-
Wreck\tTayra\t82 km''',
     [{'name': '+', 'type': 'Noctis', 'distance': '3,225 m'},
      {'name': '+', 'type': 'Thrasher', 'distance': '12 km'},
      {'name': "some dude's Stabber Fleet Issue",
       'type': 'Stabber Fleet Issue',
       'distance': '-'},
      {'name': "Wreck", 'type': 'Tayra', 'distance': '82 km'}]),
    ('test\tNoctis\t3 225 m',
     [{'name': 'test', 'type': 'Noctis', 'distance': '3 225 m'}]),
    ('', []),
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

    def test_parse_dscan(self):
        self._run_table_tests(parse_dscan, DSCAN_TABLE)
