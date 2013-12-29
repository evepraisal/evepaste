import unittest
import inspect

from evepaste import (
    parse_cargo_scan, parse_human_listing, parse_eft, parse_dscan)
from evepaste.exceptions import Unparsable


class TableTestGroup(object):
    def __init__(self, funct):
        self.funct = funct
        self.tests = []

    def add_test(self, input_str, expected, comment=None):
        self.tests.append((input_str, expected, comment))


CARGO_SCAN_TABLE = TableTestGroup(parse_cargo_scan)
CARGO_SCAN_TABLE.add_test('1 Minmatar Shuttle\n2 Gallente Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 1},
                            {'name': 'Gallente Shuttle', 'quantity': 2}], []))

CARGO_SCAN_TABLE.add_test('Minmatar Shuttle', ([], ['Minmatar Shuttle']))
CARGO_SCAN_TABLE.add_test('\n\n1 Minmatar Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 1}], []))

HUMAN_LIST_TABLE = TableTestGroup(parse_human_listing)
HUMAN_LIST_TABLE.add_test('1 Minmatar Shuttle\n2 Gallente Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 1},
                            {'name': 'Gallente Shuttle', 'quantity': 2}], []))
HUMAN_LIST_TABLE.add_test('Minmatar Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 1}], []))
HUMAN_LIST_TABLE.add_test('1x Minmatar Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 1}], []))
HUMAN_LIST_TABLE.add_test('1xMinmatar Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 1}], []))

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

DSCAN_TABLE = TableTestGroup(parse_dscan)
DSCAN_TABLE.add_test('''+\tNoctis\t3,225 m
+\tThrasher\t12 km
some dude's Stabber Fleet Issue\tStabber Fleet Issue\t-
Wreck\tTayra\t82 km''', ([
    {'name': '+', 'type': 'Noctis', 'distance': '3,225 m'},
    {'name': '+', 'type': 'Thrasher', 'distance': '12 km'},
    {'name': "some dude's Stabber Fleet Issue",
     'type': 'Stabber Fleet Issue',
     'distance': '-'},
    {'name': "Wreck", 'type': 'Tayra', 'distance': '82 km'}], []))
DSCAN_TABLE.add_test('test\tNoctis\t3 225 m', ([
    {'name': 'test', 'type': 'Noctis', 'distance': '3 225 m'}], []))
DSCAN_TABLE.add_test('', ([], []))


class TestParsers(unittest.TestCase):

    def _run_table_tests(self, table):
        for input_str, expected, comment in table.tests:
            if inspect.isclass(expected) and issubclass(expected, Exception):
                self.assertRaises(expected, table.funct, input_str)
            else:
                result = table.funct(input_str)
                self.assertEquals(result, expected, msg=comment)

    def test_cargo_scan(self):
        self._run_table_tests(CARGO_SCAN_TABLE)

    def test_parse_human_listing(self):
        self._run_table_tests(HUMAN_LIST_TABLE)

    def test_parse_eft(self):
        self._run_table_tests(EFT_TABLE)

    def test_parse_dscan(self):
        self._run_table_tests(DSCAN_TABLE)
