"""
evepaste.testing.tables.human_list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Human list table tests

"""
from evepaste import parse_human_listing
from evepaste.testing import TableTestGroup


HUMAN_LIST_TABLE = TableTestGroup(parse_human_listing)
HUMAN_LIST_TABLE.add_test('10 Minmatar Shuttle\n2 Gallente Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 10},
                            {'name': 'Gallente Shuttle', 'quantity': 2}], []))
HUMAN_LIST_TABLE.add_test('Minmatar Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 1}], []))
HUMAN_LIST_TABLE.add_test('10x Minmatar Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 10}], []))
HUMAN_LIST_TABLE.add_test('10xMinmatar Shuttle',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 10}], []))
HUMAN_LIST_TABLE.add_test('Minmatar Shuttle x 10',
                          ([{'name': 'Minmatar Shuttle', 'quantity': 10}], []))
