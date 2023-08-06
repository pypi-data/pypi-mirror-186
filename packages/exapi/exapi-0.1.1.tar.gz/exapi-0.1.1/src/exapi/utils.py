import re

snake_pattern1 = re.compile(r'([A-Z]+)([A-Z][a-z])')
snake_pattern2 = re.compile(r'(?<!^)(?<!_)(?<![A-Z])(?=[A-Z])')


def to_snake(text: str) -> str:
    return snake_pattern2.sub('_', snake_pattern1.sub(r'\1_\2', text)).lower()


def to_camel(string: str) -> str:
    return ''.join(word.capitalize() for word in string.split('_'))


def to_lower_camel(string: str) -> str:
    words = [x for x in string.split('_') if x]
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
