import re


def snake_to_camel(s: str, upper: bool = True) -> str:
    """
        Convert from snake_case to CamelCase
        If upper is set, then convert to upper CamelCase, otherwise the first character keeps its case.
    """
    _re_snake_to_camel = re.compile(r'(_)([a-z\d])')
    s = _re_snake_to_camel.sub(lambda m: m.group(2).upper(), s)
    if upper:
        s = s[:1].upper() + s[1:]
    return s


def camel_to_snake(s: str) -> str:
    """
        Convert from CamelCase to snake_case
    """
    _re_camel_to_snake = re.compile(r'([a-z]|[A-Z]+)(?=[A-Z])')
    return _re_camel_to_snake.sub(r'\1_', s).lower()
