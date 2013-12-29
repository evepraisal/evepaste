from evepaste import parse_dscan
from evepaste.testing import TableTestGroup


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
