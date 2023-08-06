import json
from typing import Union
import klsframe.utilities.utils as utils


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
