"""
evepaste.testing.tables.human_list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Human list table tests

"""
from evepaste import parse_human_listing
from evepaste.testing import TableTestGroup


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
