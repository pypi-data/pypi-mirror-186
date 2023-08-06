from datetime import datetime, date
from typing import Optional, Any


def parse_int(value: Any) -> Optional[int]:
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def age_from(birthday: Optional[datetime]) -> Optional[int]:
    if not birthday or birthday == datetime.min:
        return None
    today = date.today()
    return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
