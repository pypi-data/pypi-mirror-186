from datetime import datetime, date
from typing import Any

import pytz


def date_2_datetime(value: date, naive: bool = False) -> datetime:
    result = datetime.combine(value, datetime.min.time())
    if naive:
        return result
    return result.replace(tzinfo=pytz.UTC)


def str_2_datetime(value: str, fmt: str = '%Y-%m-%d', naive: bool = False, invalid: Any = datetime.min) -> datetime:
    try:
        result = datetime.strptime(value, fmt)
    except ValueError:
        result = invalid
    except TypeError:
        result = invalid

    if not result:
        return invalid

    if naive:
        return result
    return result.replace(tzinfo=pytz.UTC)
