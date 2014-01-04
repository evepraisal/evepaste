"""
evepaste.parsers.contract
~~~~~~~~~~~~~~~~~~~~~~~~~
Parse Contracts.

"""
import re

from evepaste.utils import regex_match_lines, f_int


CONTRACT_RE = re.compile(r"""^([\S ]*)\t     # name
                              ([\d ,\.]*)\t  # quantity
                              ([\S ]*)\t     # type
                              ([\S ]*)\t     # category
                              ([\S ]*)$      # details
                              """, re.X)
CONTRACT_RE2 = re.compile(r"""^([\S ]*)\t     # name
                               ([\d ,\.]*)\t  # quantity
                               ([\S ]*)$      # type
                               """, re.X)


def parse_contract(lines):
    """ Parse contract format

    :param string paste_string: A contract result string
    """
    matches, bad_lines = regex_match_lines(CONTRACT_RE, lines)
    matches2, bad_lines2 = regex_match_lines(CONTRACT_RE2, bad_lines)

    result = [{'name': name,
               'quantity': f_int(quantity or '1'),
               'type': _type,
               'category': category,
               'details': details,
               'fitted': details.startswith('Fitted')}
              for name, quantity, _type, category, details in matches]

    result2 = [{'name': name,
               'quantity': f_int(quantity or '1'),
               'type': _type} for name, quantity, _type in matches2]

    return result + result2, bad_lines2
