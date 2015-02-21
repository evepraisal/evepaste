"""
tests.parsers.industry
~~~~~~~~~~~~~~~~~~~~~~
Industry table tests

"""
from evepaste import parse_industry
from tests import TableTestGroup


INDUSTRY_TABLE = TableTestGroup(parse_industry)
INDUSTRY_TABLE.add_test('''Tritanium (4662 Units)
Pyerite (1857 Units)
Mexallon (1027 Units)
Isogen (44 Units)
Nocxium (51 Units)''', ([
    {'name': 'Isogen', 'quantity': 44},
    {'name': 'Mexallon', 'quantity': 1027},
    {'name': 'Nocxium', 'quantity': 51},
    {'name': 'Pyerite', 'quantity': 1857},
    {'name': 'Tritanium', 'quantity': 4662}],
    []))

INDUSTRY_TABLE.add_test('''Strontuim Clathrates (1 Unit)''',
                        ([{'name': 'Strontuim Clathrates', 'quantity': 1}],
                         []))
