"""
tests.parsers.loot_history
~~~~~~~~~~~~~~~~~~~~~~~~~~
Loot history table tests

"""
from evepaste import parse_loot_history
from tests import TableTestGroup


LOOT_HISTORY_TABLE = TableTestGroup(parse_loot_history)
LOOT_HISTORY_TABLE.add_test('''03:21:19 Some dude has looted 5 x Garde II''',
                            ([{'time': '03:21:19',
                               'player_name': 'Some dude',
                               'quantity': 5,
                               'name': 'Garde II'}], []))
LOOT_HISTORY_TABLE.add_test('''03:21:19 Some dude has looted 5 x Garde II
04:22:20 Some dude has looted 5 x Garde II''',
                            ([{'time': '03:21:19',
                               'player_name': 'Some dude',
                               'quantity': 5,
                               'name': 'Garde II'},
                              {'time': '04:22:20',
                               'player_name': 'Some dude',
                               'quantity': 5,
                               'name': 'Garde II'}], []))
LOOT_HISTORY_TABLE.add_test('Garde II', ([], ['Garde II']))
LOOT_HISTORY_TABLE.add_test('''03:21:19 A cool dude has looted 5'000 x Garde II''',
                            ([{'time': '03:21:19',
                               'player_name': 'A cool dude',
                               'quantity': 5000,
                               'name': 'Garde II'}], []))
