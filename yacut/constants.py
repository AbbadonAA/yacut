import string

SYMBOLS = string.ascii_letters + string.digits
S_LENGTH = 6
LINK_REG = r'^[a-z_A-Z\d-]{1,16}$'
FIELD_NAMES = {'original': 'url', 'short': 'custom_id'}
