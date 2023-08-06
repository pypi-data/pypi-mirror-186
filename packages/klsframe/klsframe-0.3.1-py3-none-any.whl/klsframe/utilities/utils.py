import re


def text_padding(msg, padding=2, pad_char=' ', decorator=None, decorate_lines=None):
    # TODO: chech str.rjust()
    valid_dl = [None, 'all', 'first', 'last', 'even', 'odd', []]
    if (decorator is None) ^ (decorate_lines is None):
        raise ValueError("The parameters 'decorator' and 'decorate_lines' must be used together")
    if not isinstance(padding, int):
        raise ValueError("The parameter 'padding' must be a integer number")
    counter = 0
    final = []
    for ln in msg.split('\n'):
        counter += 1
        if decorator is None:
            final.append(f'{pad_char * padding}{ln}')
        else:
            if (decorate_lines is None) or decorate_lines == '' or \
                    (isinstance(decorate_lines, list) and counter not in decorate_lines) or \
                    (decorate_lines == 'first' and counter != 1) or \
                    (decorate_lines == 'last' and counter != len(msg.split('\n'))) or \
                    (decorate_lines == 'even' and counter % 2 != 0) or \
                    (decorate_lines == 'odd' and counter % 2 == 0):
                _decorator = ' '
            elif not isinstance(decorate_lines, list) and decorate_lines not in valid_dl:
                raise ValueError("Unexpected value for parameter 'decorate_lines'")
            else:
                _decorator = decorator
            final.append(f'{pad_char * padding}{_decorator} {ln}')
    return "\n".join(final)


def assign_if_not_none(elem, if_none, if_not_none=None):
    """
    Checks if a value is None before returning it.

    If `elem` is **None**, evaluates the parameter `if_none`.
    In case of being a function, returns ``if_none(elem)``. Otherwise, returns ``if_none``


    If `elem` is **not None**, by default returns `elem`. Nevertheless, if parameter `if_not_none` is provided,
    the value returned is `if_not_none(elem)` or `if_not_none`, depending on if it is a function or not.

    Examples

    - severity = assign_if_not_none(elem=report_item.get('severity'), if_not_none=lambda x: severityDict.get(x))
    - plugin_name = assign_if_not_none(elem=report_item.get('pluginName'))
    - cpe = assign_if_not_none(elem=report_item.find("cpe"), if_not_none=lambda x: x.text, if_none='')

    :param elem: Value to be tested
    :param if_not_none: value, or function to evaluate, if ``elem`` is not None
    :param if_none: Value, or function to evaluate, if ``elem`` is None
    :return: (``elem`` | ``if_not_none`` | ``if_not_none(elem)``) if ``elem`` is not None.
            Otherwise, (``if_none`` | ``if_none(elem)``)
    """
    if elem is not None:
        if if_not_none is None:
            return elem
        else:
            return if_not_none(elem) if isfunction(if_not_none) else if_not_none
    else:
        return if_none(elem) if isfunction(if_none) else if_none


def isfunction(obj) -> bool:
    """
    Check is a variable is a function or not.

    :param obj: Reference to be tested
    :return: True if `obj` is a function or lambda. False otherwise.
    """
    return re.search('<function ', str(obj)) is not None


if __name__ == '__main__':
    # Do some quick tests here
    pass
