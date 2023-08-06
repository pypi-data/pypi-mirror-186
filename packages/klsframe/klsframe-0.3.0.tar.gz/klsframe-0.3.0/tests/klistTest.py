import klsframe.protypes.klists as _klists


def test_cast_list():
    numeros = list(range(0, 15))
    variety = [1, 2, 3, 'hola', 'adios']
    print(_klists.cast_list(numeros, float))
    print(_klists.cast_list(variety, float, _from=int))
    try:
        print(_klists.cast_list(variety, float))
        print(f"[INFO] ``test_cast_list`` failed. Exception expected")
    except ValueError:
        print(f"[INFO] Exception catched\n[INFO] ``test_cast_list`` successful")


if __name__ == '__main__':
    test_cast_list()
