import klsframe.system.system as system
import collections


def test_run_cmd():
    cmd2 = 'dir'
    cmd3 = ['ping', 'google.com']
    cmd4 = 'hatch version'
    cmd5 = 'git status'

    print(system.run_cmd(cmd2))
    print(system.run_cmd(' '.join(cmd3)))
    print(system.run_cmd(cmd4))
    print(system.run_cmd(cmd5))


def test_switch_1():
    host = {'host-ip': "10.0.0.0", 'hostname': "pepa.com", 'host-fqdn': "pepa.com", 'netbios-name': "123456",
            'operating-system': "windows", 'version': 'v0.0.0', 'last-update': '2020-20-20'}
    my_obj = collections.defaultdict.fromkeys(['ip', 'name', 'fqdn', 'netbios', 'os'], '')
    for pname, ptext in host.items():
        _cases = {
            'host-ip': f"hinfo['ip'] = {ptext}",
            'hostname': f"hinfo['name'] = {ptext}",
            'host-fqdn': f"hinfo['fqdn'] = {ptext}",
            'netbios-name': f"hinfo['netbios'] = {ptext}",
            'operating-system': f"hinfo['os'] = {ptext}"
        }
        my_obj = system.switch(pname, cases=_cases, context=my_obj, break_on='all')
    print(my_obj)


def test_switch_2():
    class Pepa:
        def __init__(self):
            self.ip = ''
            self.name = ''
            self.fqdn = ''
            self.netbios = ''
            self.os = ''

    host = {'host-ip': "10.0.0.0", 'hostname': "pepa.com", 'host-fqdn': "pepa.com", 'netbios-name': "123456",
            'operating-system': "windows", 'version': 'v0.0.0', 'last-update': '2020-20-20'}
    my_obj = Pepa()
    for pname, ptext in host.items():
        _cases = {
            'host-ip': f"hinfo.ip = {ptext}",
            'hostname': f"hinfo.name = {ptext}",
            'host-fqdn': f"hinfo.fqdn = {ptext}",
            'netbios-name': f"hinfo.netbios = {ptext}",
            'operating-system': f"hinfo.os = {ptext}"
        }
        my_obj = system.switch(pname, cases=_cases, context=my_obj, break_on='all')
    print(my_obj.__dict__)


def test_switch_3():
    _cases = {
        'saludar': f"print('Hola!')",
        'despedir': f"print('Adios!')",
        'agradecer': f"print('Gracias!')",
        'sumar': '3+2',
        'default': "print('No se que es eso')"
    }
    print("Select 1, no break ", system.switch('saludar', cases=_cases))
    print("Select 1, break 1,3 ", system.switch('saludar', cases=_cases, break_on='1,3'))
    print("Select 1, break 2,3", system.switch('saludar', cases=_cases, break_on='2,3'))
    print("Select 1, break all ", system.switch('saludar', cases=_cases, break_on='all'))
    print("Select 1, break all excep 1 ", system.switch('saludar', cases=_cases, break_on='all-1'))
    print(system.switch('sumar', cases=_cases, break_on='all'))


if __name__ == '__main__':
    test_run_cmd()
    test_switch_1()
    test_switch_2()
    test_switch_3()
    pass
