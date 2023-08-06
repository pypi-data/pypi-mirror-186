import klsframe.protypes.kstrings as _kstrings


def test_insert_str():
    print(_kstrings.insert_str('filename-javi.txt', 'MONDONGO'))
    print(_kstrings.insert_str('filename-javi.txt', 'MONDONGO', insert_before='start'))
    print(_kstrings.insert_str('filename-javi.txt', 'MONDONGO', insert_before='javi'))
    print(_kstrings.insert_str('filename-javi.txt', 'MONDONGO', insert_before='hobo'))
    print(_kstrings.insert_str('filename-javi.txt', 'MONDONGO', insert_before='w:-1', word_sep='-'))
    print(_kstrings.insert_str('filename-javi.txt', 'MONDONGO', insert_before='c:-1'))
    print(_kstrings.insert_str('Hola\nAdios', 'Que tal?', insert_before='l:-1'))


def test_join_by():
    listilla = ['Pablito', 'clavo', 3, 'clavitos']
    print(_kstrings.join_by(' + ', listilla))
    print(_kstrings.join_by(' + ', [1, 2, 3, 4, 5, 6]))


if __name__ == '__main__':
    test_insert_str()
