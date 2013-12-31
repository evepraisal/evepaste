"""
evepaste.parsers.loot_history
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Parse fleet loot history.

"""
import re

from evepaste.utils import split_and_strip, regex_match_lines, f_int

LOOT_HIST_RE = re.compile(
    r"(\d\d:\d\d:\d\d) ([\S ]+) has looted ([\d ,]+) x ([\S ]+)$")


def parse_loot_history(paste_string):
    """ Parse loot history format

    :param string paste_string: A loot history result string
    """
    paste_lines = split_and_strip(paste_string)
    matches, bad_lines = regex_match_lines(LOOT_HIST_RE, paste_lines)

    result = [{'time': time,
               'player_name': player_name,
               'quantity': f_int(quantity),
               'name': name}
              for time, player_name, quantity, name in matches]
    return result, bad_lines
