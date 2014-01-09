"""
tests.parsers.dscan
~~~~~~~~~~~~~~~~~~~
D-Scan table tests

"""
from evepaste import parse_dscan
from tests import TableTestGroup


DSCAN_TABLE = TableTestGroup(parse_dscan)
DSCAN_TABLE.add_test('''+\tNoctis\t3,225 m
+\tThrasher\t12 km
some dude's Stabber Fleet Issue\tStabber Fleet Issue\t-
Wreck\tTayra\t82 km''', ([
    {'item_name': '+', 'distance': '3,225 m', 'name': 'Noctis'},
    {'item_name': '+', 'distance': '12 km', 'name': 'Thrasher'},
    {'item_name': "some dude's Stabber Fleet Issue",
     'distance': '-',
     'name': 'Stabber Fleet Issue'},
    {'item_name': 'Wreck', 'distance': '82 km', 'name': 'Tayra'}], []))
DSCAN_TABLE.add_test('test\tNoctis\t3\xc2\xa0225 m', ([
    {'item_name': 'test', 'name': 'Noctis', 'distance': '3225 m'}], []))
DSCAN_TABLE.add_test('Otanuomi V - Moon 11\tMoon\t10.4 AU', ([
    {'item_name': 'Otanuomi V - Moon 11',
     'name': 'Moon',
     'distance': '10.4 AU'}], []))
