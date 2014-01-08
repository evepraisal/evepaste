"""
tests.parsers.chat
~~~~~~~~~~~~~~~~~~
Chat transcript table tests

"""
from evepaste import parse_chat
from tests import TableTestGroup


CHAT_TABLE = TableTestGroup(parse_chat)
CHAT_TABLE.add_test(
    '[01:46:33] Some Dude > Look, a <url=showinfo:587>Rifter</url>',
    ({'lines': [{'author': 'Some Dude',
                 'message': 'Look, a <url=showinfo:587>Rifter</url>',
                 'time': '01:46:33'}],
      'items': [{'name': 'Rifter', 'id': 587}]}, []))

CHAT_TABLE.add_test(
    '''[01:46:33] Some Dude > Look, a <url=showinfo:587>Rifter</url>
[01:46:40] Guy123 > How many <url=showinfo:587>Rifter</url>s?
[01:46:41] Some Dude > 2.
''',
    ({'items': [{'id': 587, 'name': 'Rifter'}],
      'lines': [{'author': 'Some Dude',
                 'message': 'Look, a <url=showinfo:587>Rifter</url>',
                 'time': '01:46:33'},
                {'author': 'Guy123',
                 'message': 'How many <url=showinfo:587>Rifter</url>s?',
                 'time': '01:46:40'},
                {'author': 'Some Dude', 'message': '2.', 'time': '01:46:41'}]},
     []))
