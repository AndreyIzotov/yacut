import string

SYMBOLS = string.ascii_letters + string.digits
LINK_REG = r'^[a-zA-Z\d]{1,16}$'
FIELD_NAMES = {'original': 'url', 'short': 'custom_id'}
