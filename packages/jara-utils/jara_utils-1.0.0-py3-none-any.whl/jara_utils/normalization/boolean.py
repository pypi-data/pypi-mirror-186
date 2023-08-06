import re
from typing import Optional


def str_2_bool(val: Optional[str]) -> Optional[bool]:
    if not val:
        return None
    if val.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif val.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    return None


def is_dunder(attr: str) -> bool:
    if len(attr) < 5:
        return False
    return attr.startswith('__') and attr.endswith('__')


def is_email(value: str) -> bool:
    if not value:
        return False
    user, _, domain = value.partition('@')
    if not all([user, domain]):
        return False

    user_regex = re.compile(
        r"(^[-!#$%&'*+/=?^`{}|~\w]+(\.[-!#$%&'*+/=?^`{}|~\w]+)*$"  # dot-atom
        # quoted-string
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]'
        r'|\\[\001-\011\013\014\016-\177])*"$)', re.IGNORECASE | re.UNICODE)

    domain_regex = re.compile(
        # domain
        r'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'
        r'(?:[A-Z]{2,6}|[A-Z0-9-]{2,})$'
        # literal form, ipv4 address (SMTP 4.1.3)
        r'|^\[(25[0-5]|2[0-4]\d|[0-1]?\d?\d)'
        r'(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\]$', re.IGNORECASE | re.UNICODE)

    if not user_regex.match(user):
        return False
    if not domain_regex.match(domain):
        return False
    return True
