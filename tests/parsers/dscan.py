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
    {'item_name': '+', 'name': 'Noctis', 'distance': '3,225 m'},
    {'item_name': '+', 'name': 'Thrasher', 'distance': '12 km'},
    {'item_name': "some dude's Stabber Fleet Issue",
     'name': 'Stabber Fleet Issue',
     'distance': '-'},
    {'item_name': 'Wreck', 'name': 'Tayra', 'distance': '82 km'}], []))
DSCAN_TABLE.add_test('test\tNoctis\t3 225 m', ([
    {'item_name': 'test', 'name': 'Noctis', 'distance': '3 225 m'}], []))
