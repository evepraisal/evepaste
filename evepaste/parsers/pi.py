"""
evepaste.parsers.planetary_interaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Parse planetary interaction results.

"""
import re

from evepaste.utils import regex_match_lines, f_int

PI_RE = re.compile(r"""^([\d,\.]+)\t             # quantity
                        ([\S ]+)\t               # name
                        ((Routed|Not\ routed))$  # routed
                    """, re.X)

PI_RE2 = re.compile(r"""^\t            # icon
                         ([\S ]+)\t    # name
                         ([\d,\.]+)\t  # quantity
                         ([\d,\.]+)$   # volume
                     """, re.X)

PI_RE3 = re.compile(r"""^\t            # icon
                         ([\S ]+)\t    # name
                         ([\d,\.]+)$   # quantity
                     """, re.X)


def parse_pi(lines):
    """ Parse planetary interaction results

    :param string paste_string: A PI result string
    """
    matches, bad_lines = regex_match_lines(PI_RE, lines)
    matches2, bad_lines2 = regex_match_lines(PI_RE2, bad_lines)
    matches3, bad_lines3 = regex_match_lines(PI_RE3, bad_lines2)

    result = [{'name': name,
               'quantity': f_int(quantity),
               'routed': routed == 'Routed'}
              for quantity, name, routed, _ in matches]
    result2 = [{'name': name,
                'quantity': f_int(quantity),
                'volume': volume}
               for name, quantity, volume in matches2]
    result3 = [{'name': name,
                'quantity': f_int(quantity)}
               for name, quantity in matches3]

    return result + result2 + result3, bad_lines3
