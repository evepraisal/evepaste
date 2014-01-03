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
                              ([\S ]*)$      # info
                              """, re.X)


def parse_contract(lines):
    """ Parse contract format

    :param string paste_string: A contract result string
    """
    matches, bad_lines = regex_match_lines(CONTRACT_RE, lines)

    result = [{'name': name,
               'quantity': f_int(quantity or '1'),
               'type': _type,
               'category': category,
               'info': info,
               'fitted': info.startswith('Fitted')}
              for name, quantity, _type, category, info in matches]
    return result, bad_lines
