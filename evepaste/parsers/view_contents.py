"""
evepaste.parsers.view_contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Parse results from 'View Contents' of a ship.

"""
import re

from evepaste.utils import regex_match_lines, f_int

VIEWCONT_LIST_RE = re.compile(r"""^([\S ]*)\t
                                  ([\S ]*)\t
                                  (Cargo\ Hold|
                                   Drone\ Bay|
                                   (Low|Medium|High|Rig)\ Slot|
                                   )\t
                                  ([\d ,\.]+)$""", re.X)


def parse_view_contents(lines):
    """ Parse view contents

    :param string paste_string: String pasted from view contents window
    """
    matches, bad_lines = regex_match_lines(VIEWCONT_LIST_RE, lines)

    result = [{'name': name,
               'group': group,
               'location': location,
               'quantity': f_int(quantity)}
              for (name,
                   group,
                   location, _,
                   quantity) in matches]
    return result, bad_lines
