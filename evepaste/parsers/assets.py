"""
evepaste.parsers.assets
~~~~~~~~~~~~~~~~~~~~~~~
Parse eve online asset lists. This also invludes inventory listings.

"""
import re

from evepaste.utils import regex_match_lines, f_int

ASSET_LIST_RE = re.compile(r"""^([\S ]*)                           # name
                                \t([\d,\.]*)                       # quantity
                                (\t([\S ]*))?                      # group
                                (\t([\S ]*))?                      # category
                                (\t(XLarge|Large|Medium|Small|))?  # size
                                (\t(High|Medium|Low|Rigs|[\d ]*))? # slot
                                (\t([\d ,\.]* m3))?                # volume
                                (\t([\d]+|))?                      # meta level
                                (\t([\d]+|))?$                     # tech level
                               """, re.X)


def parse_assets(lines):
    """ Parse asset list

    :param string paste_string: An asset list string
    """
    matches, bad_lines = regex_match_lines(ASSET_LIST_RE, lines)

    result = [{'name': name,
               'quantity': f_int(quantity) or 1,
               'group': group,
               'category': category,
               'size': size,
               'slot': slot,
               'volume': volume,
               'meta_level': meta_level,
               'tech_level': tech_level}
              for (name,
                   quantity,
                   _, group,
                   _, category,
                   _, size,
                   _, slot,
                   _, volume,
                   _, meta_level,
                   _, tech_level) in matches]
    return result, bad_lines
