import json
from typing import Union
import re
import klsframe.protypes.kstrings as _kstr


def save_json(obj, filepath, indent=2) -> None:
    if obj is not None and filepath is not None:
        with open(filepath, 'w') as file:
            json.dump(obj, file, indent=int(indent))


def load_json(filepath) -> Union[dict, list]:
    if filepath is not None:
        with open(filepath, 'r') as file:
            return json.load(file)


def save_yaml(obj, filepath) -> int:
    pass


def load_yaml(filepath) -> Union[dict, list]:
    pass


def save_file(filename, dir='.', fullpath=None, ext=''):
    """
    TODO: save_file()
    Saves a file
    :param filename: Name for the file
    :param dir: directory where the file is saved. The default value is the current dir
    :param ext: File extension. By default, no extension is used, like in linux files
    :return: 0 on success. 1 on failure
    """
    # if filename is a path and is different from dir we are in troubles
    # if utils.validate(filename, []):


def append_to_filename(fname, value, insert_before='end'):
    """
    Appends a value to a filename (or full path)

    Example

    - recon_usuarios-2022_02_02-20_20.xml --> recon_usuarios-chunk3-2022-02-02-20_20.xml

    :param fname: File name (or full path) to be modified
    :param value: Value to be inserted into the file name. By default, ``step`` is an int, but it can be any str
    :param insert_before: Position where ``value`` should be placed. Check `utils.insert_str` for more info
    :return: A new string, resulting from inserting `value` into `fname` at the position `insert_before`
    """
    split = fname.split('\\')  # Separate the path from file name
    if re.fullmatch('^([.\\-\\w])+[.](\\w)+$', split[-1]) is not None:  # File ext included in the name
        name_split = split[-1].split('.')  # Split the file name to remove the extension
        name_split[-2] = _kstr.insert_str(name_split[-2], value=value, insert_before=insert_before)
        split[-1] = ".".join(name_split)
    else:  # File ext not included in the file name
        split[-1] = _kstr.insert_str(split[-1], value=value, insert_before=insert_before)
    return '\\'.join(split)
