"""
evepaste.parsers.bill_of_materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Parse Bill of Materials.

"""
import re

from evepaste.utils import regex_match_lines, f_int

BOM_RE = re.compile(r"^([\S ]+) - \[You: (\d+)( - Perfect: (\d+))?\]$")
BOM_RE2 = re.compile(r"^([\S ]+) \[([\d]+)\]$")
IGNORED_LINES = ['Bill of Materials does not take into consideration the '
                 'efficiency of an installation.',
                 'Extra Materials are not affected by skills and are not '
                 'returned when recycling the manufactured product.',
                 'No Item']


def parse_bill_of_materials(lines):
    """ Parse bill of materials

    :param string paste_string: A bill of material string
    """
    matches, bad_lines = regex_match_lines(BOM_RE, lines)
    matches2, bad_lines2 = regex_match_lines(BOM_RE2, bad_lines)

    result = [{'name': name,
               'you': f_int(you),
               'perfect': f_int(perfect or you)}
              for name, you, _, perfect in matches]
    result2 = [{'name': name,
                'quantity': f_int(quantity)}
               for name, quantity in matches2]
    results = result + result2
    if results:
        for line in IGNORED_LINES:
            if line in bad_lines2:
                bad_lines2.remove(line)

    return results, bad_lines2
