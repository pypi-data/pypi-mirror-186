import klsframe.utilities.serializer as _kser


def test_chunk_file_name():
    chunk_range = range(1, 4)
    for i in chunk_range:
        print("Custom regex :", _kser.append_to_filename('soy-un-fichero.txt', i, insert_before='\\-un\\-'))
    print(f"{'-' * 35}")
    for i in chunk_range:
        print("Start :", _kser.append_to_filename('soy-un-fichero.txt', i, insert_before='start'))
    print(f"{'-' * 35}")
    for i in chunk_range:
        print("End (with file ext): ", _kser.append_to_filename('soy-un-fichero.txt', i))
    print(f"{'-' * 35}")
    for i in chunk_range:
        print("End (without file ext): ", _kser.append_to_filename('soy-un-fichero', i))
    print(f"{'-' * 35}")
    print("End (custom chunk_rep): ", _kser.append_to_filename('soy-un-fichero.txt', value='blabla'))
    print(f"{'-' * 35}")
    print("End (custom chunk_rep and step): ",
          _kser.append_to_filename('soy-un-fichero.txt', value='pan'))
    _datetime_regex = '\\-[0-9]{4}(_[0-9]{2}){2}\\-[0-9]{2}_[0-9]{2}'
    print(f"{'-' * 35}")
    for i in chunk_range:
        print("End (custom chunk_rep): ",
              _kser.append_to_filename('soy-un-fichero-2022_02_02-12_14.txt', value=f"-tramo{i}",
                                       insert_before=_datetime_regex))


if __name__ == '__main__':
    test_chunk_file_name()
