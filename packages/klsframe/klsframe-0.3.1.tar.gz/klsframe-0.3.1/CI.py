import re
import argparse
import klsframe.system.system as system


def _parse_args():
    parser = argparse.ArgumentParser(
        prog='Continuous integration - Git - Pypi',
        description='Builds, push to the repo and publish a new version of the module'
    )
    parser.add_argument('version', help='New version for the module')
    return parser.parse_args()


if __name__ == '__main__':
    __args__ = _parse_args()
    assert re.fullmatch('([0-9]+\\.){0,2}[0-9]+', __args__.version) is not None, "Invalid version syntax"
    steps = [
        f'hatch version {__args__.version}',
        f"git add .", f'git commit -am "{__args__.version}"',
        f'hatch build', f'hatch publish'
    ]
    for st in steps:
        system.run_cmd(st)
