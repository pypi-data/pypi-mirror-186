import os
import time

import pandas as pd
import klsframe.utilities.dataframe as dfutils


def test_multi_merge():
    _test_error = f"[FAIL] `test_multi_merge` failed"
    df1 = pd.DataFrame({'team': ['A', 'B', 'C', 'D'], 'points': [18, 22, 19, 14]})
    df2 = pd.DataFrame({'team': ['A', 'B', 'C'], 'assists': [4, 9, 14]})
    df3 = pd.DataFrame({'team': ['C', 'D', 'E', 'F'], 'rebounds': [10, 17, 11, 10]})
    try:
        dfutils.multi_merge(df1, on='team')
    except TypeError as e:
        assert str(e) == "Invalid type for parameter 'dataframes'. Allowed: list", _test_error
    try:
        dfutils.multi_merge([df1], on='team')
    except IndexError as e:
        assert str(e) == "Not enough dataframes to merge. At least 2 dataframes are required", _test_error
    result_1 = dfutils.multi_merge([df1, df2, df3], on='team', how='outer')
    expected = pd.DataFrame({'team': ['A', 'B', 'C', 'D', 'E', 'F'], 'points': [18, 22, 19, 14, None, None],
                             'assists': [4, 9, 14, None, None, None], 'rebounds': [None, None, 10, 17, 11, 10]})
    assert result_1.to_string() == expected.to_string(), _test_error
    print(expected.groupby('team'))
    print(expected.groupby('team').size())
    print(expected.groupby('team').size().reset_index(name='Teemo'))
    print(f"[OK] `test_multi_merge` successful")


def test_class_df_collection():
    df1 = pd.DataFrame({'team': ['A', 'B', 'C', 'D'], 'points': [18, 22, 19, 14]})
    df2 = pd.DataFrame({'team': ['A', 'B', 'C'], 'assists': [4, 9, 14]})
    df3 = pd.DataFrame({'team': ['C', 'D', 'E', 'F'], 'rebounds': [10, 17, 11, 10]})
    coll = dfutils.DataFrameCollection.fromkeys(['faltas'])
    coll.add('fueras de juego')
    coll.add('puntos', df1)
    coll.update({'asistencias': df2, 'rebotes': df3})
    print(coll)
    coll.to_excel('testing', exclude='mondongo')
    os.remove('testing.xlsx')
    b = dfutils.DataFrameCollection({'page1': pd.DataFrame(), 'page2': pd.DataFrame()})
    print(b)
    b = dfutils.DataFrameCollection(page1=pd.DataFrame(), page2=pd.DataFrame())
    print(b.__repr__())
    print(f"[OK] `test_class_df_collection` successful")


def test_class_df_collection_2():
    df1 = pd.DataFrame({'team': ['A', 'B', 'C', 'D'], 'points': [18, 22, 19, 14]})
    df2 = pd.DataFrame({'team': ['A', 'B', 'C'], 'assists': [4, 9, 14]})
    df3 = pd.DataFrame({'team': ['C', 'D', 'E', 'F'], 'rebounds': [10, 17, 11, 10]})
    coll = dfutils.DataFrameCollection({'puntos': df1, 'asistencias': df2, 'rebotes': df3})
    print(coll.combine(on='team', how='outer'))
    try:
        print(coll.combine(on='team', how='outer', include='puntos'))
    except IndexError as e:
        assert str(e) == "Not enough dataframes to merge. At least 2 dataframes are required"
    print(coll.combine(on='team', how='outer', include=['puntos', 'rebotes']))
    print(coll.combine(on='team', how='outer', exclude='rebotes'))
    try:
        print(coll.combine(on='team', how='outer', exclude=['rebotes', 'asistencias']))
    except IndexError as e:
        assert str(e) == "Not enough dataframes to merge. At least 2 dataframes are required"
    try:
        coll.combine(on='team', how='outer', include='puntos', exclude=['rebotes', 'asistencias'])
    except ValueError as e:
        assert str(e) == "Parameters 'include' and 'exclude' are mutually exclusive and cannot be use together"
    print(f"[OK] `test_class_df_collection_2` successful")


if __name__ == '__main__':
    test_multi_merge()
    test_class_df_collection()
    time.sleep(2)
    test_class_df_collection_2()
