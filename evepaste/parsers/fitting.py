"""
evepaste.parsers.fitting
~~~~~~~~~~~~~~~~~~~~~~~~
Parse saved fittings.

"""
from evepaste.exceptions import Unparsable
from evepaste.parsers.listing import parse_listing
from evepaste.utils import split_and_strip


FITTING_BLACKLIST = ['High power',
                     'Medium power',
                     'Low power',
                     'Rig Slot',
                     'Sub System',
                     'Charges',
                     'Drones']


def parse_fitting(paste_string):
    """ Parse Fitting List

    :param string paste_string: A new-line separated list of items
    """
    paste_lines = split_and_strip(paste_string)

    is_fitting_listing = False
    for item in FITTING_BLACKLIST:
        if item in paste_lines:
            paste_lines.remove(item)
            is_fitting_listing = True

    if is_fitting_listing is False:
        raise Unparsable('Not a fitting list')

    return parse_listing('\n'.join(paste_lines))
