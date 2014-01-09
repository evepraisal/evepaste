"""
evepaste.parsers.survey_scanner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Parse survey scanner results.

"""
import re

from evepaste.utils import regex_match_lines, f_int

SURVEY_SCANNER_RE = re.compile(r"""^([\S ]+)\t           # name
                                    ([\d,\.]+)\t         # quantity
                                    ([\d,\.]*\ (m|km))$  # distance
                                """, re.X)


def parse_survey_scanner(lines):
    """ Parse survey scanner

    :param string paste_string: A survey scanner result string
    """
    matches, bad_lines = regex_match_lines(SURVEY_SCANNER_RE, lines)

    result = [{'name': name,
               'quantity': f_int(quantity),
               'distance': distance}
              for name, quantity, distance, _ in matches]  # NOQA (F812)
    if matches:
        return result, []
    else:
        return result, bad_lines
