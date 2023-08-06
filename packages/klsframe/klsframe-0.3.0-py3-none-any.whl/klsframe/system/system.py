from datetime import datetime
from glob import glob
import os
import sys
import re
import klsframe.utilities.utils as utils
from klsframe.protypes.klists import cast_list


def run_cmd(command: str):
    if not isinstance(command, str):
        raise TypeError("Invalid type for parameter 'command'. Allowed: str")
    filename = f"{str(datetime.now().timestamp()).replace('.', '_')}-kls"
    if sys.platform == 'win32':
        redirect = f'{os.getenv("TMP")}\\{filename}'
        encoding = 'cp858'
    else:
        redirect = f'{os.getenv("home")}/tmp/{filename}'
        encoding = 'utf-8'
    os.system(f"{command} > {redirect}")
    try:
        with open(redirect, 'r', encoding=encoding) as stdout:
            return stdout.read()
    except FileNotFoundError:
        return "The output of the command could not be retrieved"


def find_files(rootdir=None, regex=None):
    """
    Find files in a folder. Regex can be applied in the file name

    :param rootdir: Root dir to search for the files. If None, the current dir is used
    :param regex: Regex to be matched against the file names. If None, wild card * is used
    :return: A list of the file names (not full path) from the directory ```rootdir``, that are matching the ``regex``
    """
    if rootdir is None:
        rootdir = '.'
    if regex is None:
        regex = '*'
    return glob(os.path.join(rootdir, regex))


class Switch:
    # TODO switch class
    class SwitchCase:
        def __init__(self):
            self.condition = ''
            self.actions = []
            self._break = False

        def add_action(self, action: str):
            self.actions.append(action)

        def exec(self):
            for act in self.actions:
                if utils.isfunction(act):
                    act()
                else:
                    eval(str(act))
            if self._break:
                return

    def __init__(self):
        self.value = None
        self.cases = {}
        self.default = None
        self.break_on = set()
        self.context = {}

    def add_case(self, cskey, csvalue):
        self.cases.update({cskey: csvalue})

    def set_default(self, default_option):
        self.default = default_option

    def add_to_context(self, **kwargs):
        self.context.update(kwargs)


def switch(value, cases: dict, default=None, break_on=None, context=None):
    """
    TODO: switch()
    Class Switch. Allows to create a complex switch. You can add variables to the Switch.context to operate with them
    This function requires a context to work properly. Otherwise it cannot understand references to other objects
    value = pname
    cases = {
        'host-ip': "hinfo['ip'] = ptext",
        'hostname': "hinfo['name'] = ptext",
        'host-fqdn': "hinfo['fqdn'] = ptext",
        'netbios-name': "hinfo['netbios'] = ptext",
        'operating-system': "hinfo['os'] = ptext",
        'default': ''
    }

    :param context:
    :param value:
    :param cases:
    :param default:
    :param break_on: (None|'1,2,4'|'all'|'all-1')
    :return:
    """
    # TODO: convertir break_on a una lista de enteros

    if break_on is None:
        break_on = []
    elif isinstance(break_on, str) and re.fullmatch('((all-)?([0-9]+,)?[0-9]+)|all', break_on):
        _all = range(0, len(cases.keys()))
        if break_on.startswith('all-'):
            break_on = list(set(_all) - set(cast_list(break_on[4:].split(','), int)))
        elif break_on.startswith('all'):
            break_on = _all
        else:
            break_on = cast_list(break_on.split(','), int)
    else:
        raise TypeError("Invalid syntax for parameter 'break_on'. Check the docs for further information")
    if 'default' in cases:
        default = cases.pop('default')
    for ind, (cskey, csval) in enumerate(cases.items(), 1):
        if value == cskey:
            if re.fullmatch("\\w+\\['\\w+'\\] *= *[\\.\\w]+", csval) is not None:
                _csval_right_expr = re.search("= *[\\.\\w]+", csval)[0][1:].strip()
                keystr = re.search("'\\w+'", csval)[0][1:-1]
                eval(f"context.update(collections.defaultdict.fromkeys(['{keystr}'], '{_csval_right_expr}'))")
            elif re.fullmatch("\\w+(\\.\\w+)+ *= *[\\.\\w]+", csval) is not None:
                _csval_right_expr = re.search("= *[\\.\\w]+", csval)[0][1:].strip()
                field = re.search('(\\.\\w+)+', csval)[0][1:]
                eval(f"context.__setattr__('{field}', '{_csval_right_expr}')")
            else:
                context = eval(str(csval))
            if ind in break_on:
                return context
    if default is not None:
        eval(str(default))
    return context
