"""
evepaste.parsers.view_contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Parse results from 'View Contents' of a ship.

"""
from collections import defaultdict
import re

from evepaste.utils import regex_match_lines, f_int

VIEWCONT_LIST_RE = re.compile(r"""^([\S ]*)\t
                                  ([\S ]*)\t
                                  (Cargo\ Hold|
                                   (Drone|Fuel)\ Bay|
                                   (Low|Medium|High|Rig)\ Slot|
                                   Subsystem|
                                   )\t
                                  ([\d,\.]+)$""", re.X)
STATION_CONTAINER_RE = re.compile(r"""^([\S ]*)\t
                                       ([\S ]*)\t
                                       ([\d,\.]+)$""", re.X)


def parse_view_contents(lines):
    """ Parse view contents

    :param string paste_string: String pasted from view contents window
    """
    matches, bad_lines = regex_match_lines(VIEWCONT_LIST_RE, lines)
    matches2, bad_lines2 = regex_match_lines(STATION_CONTAINER_RE, bad_lines)

    items = defaultdict(int)
    for name, group, location, _, _, quantity in matches:
        items[(name, group, location)] += f_int(quantity)

    results = [{'name': name,
                'group': group,
                'location': location,
                'quantity': quantity}
               for (name, group, location), quantity in sorted(items.items())]

    items2 = defaultdict(int)
    for name, group, quantity in matches2:
        items2[(name, group)] += f_int(quantity)
    results2 = [{'name': name,
                 'group': group,
                 'quantity': quantity}
                for (name, group), quantity in sorted(items2.items())]

    return results + results2, bad_lines2
