import random
from string import ascii_letters, digits

from .constants import SYMBOLS
from .models import URL_map


def get_unique_short_id(list=ascii_letters + digits, k=6):
    short_id = ''.join(random.choice(SYMBOLS) for i in range(6))
    if check_short_id(short_id):
        return short_id
    return get_unique_short_id()


def get_db_object(column, query):
    return URL_map.query.filter(column == query)


def check_short_id(short_id):
    if get_db_object(URL_map.short, short_id).first() is None:
        return True
    return False
