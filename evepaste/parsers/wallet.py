"""
evepaste.parsers.wallet
~~~~~~~~~~~~~~~~~~~~~~~
Parse wallet results.

"""
import re

from evepaste.utils import regex_match_lines, f_int

JOURNAL_RE = re.compile(r"""^(\d\d\d\d.\d\d.\d\d\ \d\d:\d\d:\d\d)\t  # time
                             ([\S ]+)\t                # transaction type
                             ([-\d,\.]+\ (ISK|AUR))\t  # amount
                             ([\d,\.]+\ (ISK|AUR))\t   # balance
                             ([\S ]*)$                 # description
                         """, re.X)

TRANSACTION_RE = re.compile(r"""^(\d\d\d\d.\d\d.\d\d\ \d\d:\d\d)\t  # when
                             ([\S ]+)\t                # name
                             ([\d,\.]+\ (ISK|AUR))\t   # price
                             ([\d,\.]+)\t              # quantity
                             ([-\d,\.]+\ (ISK|AUR))\t  # credit
                             (ISK|AUR)\t               # currency
                             ([\S ]+)\t                # client
                             ([\S ]+)$                 # where
                         """, re.X)


def parse_wallet(lines):
    """ Parse wallet

    :param string paste_string: A swallet result string
    """
    matches, bad_lines = regex_match_lines(JOURNAL_RE, lines)
    matches2, bad_lines2 = regex_match_lines(TRANSACTION_RE, bad_lines)

    result = [{'time': time,
               'transaction_type': transaction_type,
               'amount': amount,
               'balance': balance,
               'description': desc}
              for (time,
                   transaction_type,
                   amount, _,
                   balance, _,
                   desc) in matches]
    result2 = [{'time': time,
                'name': name,
                'price': price,
                'quantity': f_int(quantity),
                'credit': credit,
                'currency': currency,
                'client': client,
                'where': where}
               for (time,
                    name,
                    price, _,
                    quantity,
                    credit, _,
                    currency,
                    client,
                    where) in matches2]

    return result + result2, bad_lines2
