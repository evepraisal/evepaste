"""
tests.parsers.planetary_interaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
planetary interaction list table tests

"""
from evepaste import parse_pi
from tests import TableTestGroup


PI_TABLE = TableTestGroup(parse_pi)

PI_TABLE.add_test('''331.0\tAqueous Liquids\tNot routed
331\tAqueous Liquids\tRouted''', ([
                  {'routed': False,
                   'name': 'Aqueous Liquids',
                   'quantity': 3310},
                  {'routed': True,
                   'name': 'Aqueous Liquids',
                   'quantity': 331}], []))
PI_TABLE.add_test('''\tAqueous Liquids\t305.0\t3.05''', ([
                  {'volume': '3.05',
                   'name': 'Aqueous Liquids',
                   'quantity': 3050}], []))
PI_TABLE.add_test('''\tAqueous Liquids\t205.0''', ([
                  {'name': 'Aqueous Liquids', 'quantity': 2050}], []))
