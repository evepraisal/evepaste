"""
evepaste.parsers.bill_of_materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Parse Bill of Materials.

"""
import re

from evepaste.utils import split_and_strip, regex_match_lines, f_int

BOM_RE = re.compile(r"^([\S ]+) - \[You: (\d+) - Perfect: (\d+)\]$")
BOM_RE2 = re.compile(r"^([\S ]+) \[([\d]+)\]$")


def parse_bill_of_materials(paste_string):
    """ Parse bill of materials

    :param string paste_string: A bill of material string
    """
    paste_lines = split_and_strip(paste_string)
    matches, bad_lines = regex_match_lines(BOM_RE, paste_lines)
    matches2, bad_lines2 = regex_match_lines(BOM_RE2, bad_lines)

    result = [{'name': name,
               'you': f_int(you),
               'perfect': f_int(perfect)}
              for name, you, perfect in matches]
    result2 = [{'name': name,
                'quantity': f_int(quantity)}
               for name, quantity in matches2]
    return result + result2, bad_lines2
