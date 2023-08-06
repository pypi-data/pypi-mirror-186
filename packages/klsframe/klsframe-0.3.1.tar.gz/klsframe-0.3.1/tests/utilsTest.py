import klsframe.utilities.utils as utils


def test_assign_if_not_none():
    import xml.etree.ElementTree as Et
    eo = Et.Element('cve', attrib={'port': '8080'})
    eo.text = 'hola'
    val1 = utils.assign_if_not_none(eo.get('port'), if_none='')
    val2 = utils.assign_if_not_none(eo, if_none='', if_not_none=lambda x: x.text)
    val3 = utils.assign_if_not_none(eo.get('host'), if_none='')
    assert val1 == '8080' and val2 == 'hola' and val3 == ''
    print(f"[INFO] Test `test_assign_if_not_none` successful")


if __name__ == '__main__':
    test_assign_if_not_none()
