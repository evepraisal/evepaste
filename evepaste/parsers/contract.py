"""
evepaste.parsers.contract
~~~~~~~~~~~~~~~~~~~~~~~~~
Parse Contracts.

"""
from collections import defaultdict
import re

from evepaste.utils import regex_match_lines, f_int


CONTRACT_RE = re.compile(r"""^([\S ]*)\t     # name
                              ([\d,\.]*)\t   # quantity
                              ([\S ]*)\t     # type
                              ([\S ]*)\t     # category
                              ([\S ]*)$      # details
                              """, re.X)
CONTRACT_RE2 = re.compile(r"""^([\S ]*)\t     # name
                               ([\d,\.]*)\t   # quantity
                               ([\S ]*)$      # type
                               """, re.X)


def parse_contract(lines):
    """ Parse contract format

    :param string paste_string: A contract result string
    """
    matches, bad_lines = regex_match_lines(CONTRACT_RE, lines)
    matches2, bad_lines2 = regex_match_lines(CONTRACT_RE2, bad_lines)

    # Collect Items
    items = defaultdict(int)
    for name, quantity, _type, category, details in matches:
        items[(name, _type, category, details)] += f_int(quantity) or 1

    result = [{'name': name,
               'quantity': quantity,
               'type': _type,
               'category': category,
               'details': details,
               'fitted': details.startswith('Fitted')}
              for (name, _type, category, details), quantity
              in sorted(items.items())]

    # Collect Items2
    items2 = defaultdict(int)
    for name, quantity, _type in matches2:
        items2[(name, _type)] += f_int(quantity) or 1

    result2 = [{'name': name,
                'quantity': quantity,
                'type': _type} for (name, _type), quantity in items2.items()]

    return result + result2, bad_lines2
