import datetime
import decimal
from .pset import pset


def Boolean(s):
    return s.lower() in ('true', 'yes', '1') if isinstance(s, str) else bool(s)


def NOK(s):
    return decimal.Decimal(s.replace(',', '.'))


def Datetime(s):
    try:
        return datetime.datetime.strptime(s, '%Y-%m-%d %H:%M')
    except:  # noqa
        return None


def Date(s):
    try:
        return datetime.datetime.strptime(s, '%Y-%m-%d')
    except:    # noqa
        return None


class xmlrec(pset):
    convert = {
        'date': Date,
        'datetime': Datetime,
        'int': int,
        'bool': Boolean,
        'NOK': NOK,
    }

    def __init__(self, soup, **types):
        super().__init__()
        for tag in soup.findAll(True):
            name = str(tag.name).lower()
            val = tag.string
            if name in types:
                t = types[name]
                if t in self.convert:
                    val = self.convert[t](val)
            elif 'all' in types:
                t = types['all']
                if t in self.convert:
                    val = self.convert[t](val)
            self[name] = val
