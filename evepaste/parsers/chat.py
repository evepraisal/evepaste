"""
evepaste.parsers.chat
~~~~~~~~~~~~~~~~~~~~~
Parse Chat transcripts.

"""
import re

from evepaste.utils import regex_match_lines, f_int

CHAT_RE = re.compile(r"^(\[(\d\d:\d\d:\d\d)\] )?([\S ]+?) > (.*)$")
CHAT_ITEM_RE = re.compile(r"<url=showinfo:([\d]+?)>([\S ]+?)</url>")


def parse_chat(lines):
    """ Parse Chat transcript

    :param string paste_string: Chat transcript string
    """
    matches, bad_lines = regex_match_lines(CHAT_RE, lines)

    lines = [{'time': time, 'author': author, 'message': message}
             for _, time, author, message in matches]

    items = {}
    if lines:
        for line in lines:
            item_matches = CHAT_ITEM_RE.findall(line['message'])
            for item_id, name in item_matches:
                if item_id not in item_matches:
                    items[item_id] = {'id': f_int(item_id), 'name': name}

        return {'lines': lines, 'items': sorted(items.values())}, bad_lines
    else:
        return None, bad_lines
