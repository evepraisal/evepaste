"""
tests.parsers.survey_scanner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
survey scanner list table tests

"""
from evepaste import parse_survey_scanner
from tests import TableTestGroup


SURVEY_SCANNER_TABLE = TableTestGroup(parse_survey_scanner)

SURVEY_SCANNER_TABLE.add_test(
    '''Pyroxeres\t1,919\t5,842 m
Pyroxeres\t11,595\t7,180 m
Pyroxeres\t5,414\t6,134 m
Scordite
Veldspar
Veldspar\t10\t12 km
Veldspar\t26,644\t6,115 m
Veldspar\t26,935\t12 km
''',
    ([{'distance': '5,842 m', 'name': 'Pyroxeres', 'quantity': 1919},
      {'distance': '7,180 m', 'name': 'Pyroxeres', 'quantity': 11595},
      {'distance': '6,134 m', 'name': 'Pyroxeres', 'quantity': 5414},
      {'distance': '12 km', 'name': 'Veldspar', 'quantity': 10},
      {'distance': '6,115 m', 'name': 'Veldspar', 'quantity': 26644},
      {'distance': '12 km', 'name': 'Veldspar', 'quantity': 26935}], []))
