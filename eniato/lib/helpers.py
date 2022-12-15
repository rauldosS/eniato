import decimal
import locale

from dateutil.parser import parse

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

EMPTY_VALUES = [None, '']


def decimal_or_none(obj, key=None):
    if key is not None:
        value = obj.get(key)
    else:
        value = obj

    if value in EMPTY_VALUES:
        return None
    return decimal.Decimal(value)


def decimal_or_zero(obj, key=None):
    if key is not None:
        value = obj.get(key)
    else:
        value = obj

    if value in EMPTY_VALUES:
        return decimal.Decimal(0)
    return decimal.Decimal(value)


def date_or_none(value):
    try:
        return parse(value).date()
    except (ValueError, TypeError):
        return None


def datetime_or_none(value):
    try:
        return parse(value)
    except (ValueError, TypeError):
        return None

def local_currency(value, grouping=True, symbol=True):
    return locale.currency(value, grouping=grouping, symbol=symbol)
