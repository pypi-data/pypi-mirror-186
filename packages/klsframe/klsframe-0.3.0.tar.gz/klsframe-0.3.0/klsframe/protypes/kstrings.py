import re
import klsframe.utilities.utils as _utils


def equals_ignore_case(str1, str2):
    return re.fullmatch(str1, str2, flags=re.IGNORECASE) is not None


def validate(value, validations):
    if validations is None:
        raise ValueError("Validations cannot be None")
    elif not isinstance(validations, list):
        validations = [validations]
    if len(validations) == 0:
        return True
    else:
        for valid in validations:
            if re.fullmatch(valid, value) is not None:
                return True
        return False


def join_by(join_char, iterable):
    """
    Joins an <iterable> with <join_char>. Uses list-comprehension
    :param join_char: Char to be used as join
    :param iterable: Iterable to be joined using <join_char>
    :return: A string with all the elements of <iterable> joined by <join_char>
    """
    return str(join_char).join([str(val) for val in iterable])


def insert_str(original: str, value, insert_before='end', word_sep=' '):
    """
    Inserts a given value, in a certain position, of a given string.
    The position (parameter ``insert_before``) is a string with multiple formats:

    - 'start': insert at the very beginning of the string
    - 'end': insert at the very end of the string
    - 'c:<num>' Character index (starts at 0, supports negative indexes)
    - 'w:<num>' Word index (starts at 0, supports negative indexes). Words are separated by `word_sep`
    - 'l:<num>' Line index (starts at 0, supports negative indexes). Lines are separated by '\n'

    :param original: Original string
    :param value: to be inserted. Can be a string, a function or lambda
    :param insert_before: ('start'|'end'|'c:1'|'w:1'|'l:1'|custom_regex) specifies where to insert the provided value
    :param word_sep: Char separating words (if more than one) in string `original`.
            Only used when `insert_before` starts with 'w:'
    :return: `Original` string with `value` inserted (if the conditions matched)
    """
    value = value(original) if _utils.isfunction(value) else str(value)
    try:
        re.compile(insert_before)
    except re.error as e:
        raise SyntaxError(f"Invalid regex syntax. {str(e).capitalize()}")
    try:
        if insert_before == 'start':
            return f"{value}{original}"
        elif insert_before == 'end':
            return f"{original}{value}"
        elif insert_before.startswith('c:'):  # Character split
            ind = int(insert_before[2:])
            return f"{original[0:ind]}{value}{original[ind:]}"
        elif insert_before.startswith('w:'):  # Word split
            ind = int(insert_before[2:])
            split = original.split(word_sep)
            split[ind] = f"{value}{split[ind]}"
            return word_sep.join(split)
        elif insert_before.startswith('l:'):  # Line split
            ind = int(insert_before[2:])
            split = original.split('\n')
            split.insert(ind, str(value))
            return '\n'.join(split)
        elif re.search(insert_before, original) is not None:  # Custom insert_at
            return re.sub(insert_before, f"{value}{re.search(insert_before, original)[0]}", original)
        else:
            print(f"[WARN] Regex '{insert_before}' not found within the string '{original}'")
            return str(original)
    except ValueError as e:
        raise ValueError(f"Bad split keyword ('{insert_before}'). Expected '{insert_before}<num>'\n{e}")
