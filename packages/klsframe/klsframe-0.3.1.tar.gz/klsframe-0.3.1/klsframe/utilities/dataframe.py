import collections
import copy
from functools import reduce
from typing import Union

import pandas as pd
import re

from klsframe.protypes import klists as _klists
import klsframe.utilities.utils as _kutils


class DataFrameCollection(dict):
    """
    Custom collection, extending from `dict`, whose keys represent page names and the values pandas DataFrames.
    It is similar to an Excel book, but only in-memory and uses DataFrames instead of Excel workbooks.
    This class eases data export (to Excel), printing, merging... it can be seen as a workspace for dataframes
    """

    def __init__(self, seq=None, **kwargs):
        super().__init__(**kwargs)
        if seq is None:
            pass
        elif isinstance(seq, dict):
            self.update(seq)
        else:
            raise TypeError("Invalid type for initializing DataFrameCollection. Allowed: dict")

    def __repr__(self):
        return f"DataFrameCollection({[k for k in self.keys()]})"

    def __str__(self):
        _str = ""
        for ind, (dfname, dfcontents) in enumerate(self.items(), 1):
            _str += f"Page '{dfname}'\n\n{dfcontents}\n{'-' * 18} pg {ind} {'-' * 18}\n"
        return _str

    def to_string(self):
        _str = ""
        for ind, (dfname, dfcontents) in enumerate(self.items(), 1):
            _str += f"Page '{dfname}'\n\n{dfcontents.to_string()}\n{'-' * 18} pg {ind} {'-' * 18}\n"
        return _str

    def add(self, dfname, dfdata=None):
        if dfname in self:
            raise KeyError(f"The dataframe already exists. If you want to update its value use `update()` function")
        else:
            self.update({dfname: dfdata if dfdata is not None else pd.DataFrame()})

    def to_excel(self, outfile, exclude=None) -> None:
        """
        Saves the content of this DataFrameCollection instance into an Excel book

        :param outfile: Name for the output Excel book (file extension not needed, it is implicit)
        :param exclude: List containing the page names excluded of the output Excel book.
                If None, no pages are excluded. If this param contains a page name that does not exist
                within this `DataFrameCollection` instance, the user will be warned and the page name skipped,
                causing no exception
        :return: None
        """
        exclude = _kutils.assign_if_not_none(exclude, if_not_none=lambda x: _klists.list_wrap(x), if_none=[])
        aux = copy.deepcopy(self)
        for dfname in exclude:
            try:
                aux.pop(dfname)
            except KeyError:
                print(f"[WARN] The specified df ('{dfname}') in not included in this collection")
        df_to_excel(outfile, aux)

    def combine(self, on: Union[str, list], include=None, exclude=None, **kwargs):
        """
        Combine the dataframes included in this instance of `DataFrameCollection`

        :param on: Column(s) on which the merge will be applied
        :param include: Pages to be included. Cannot be used together with ``exclude``
        :param exclude: Pages to be excluded. Cannot be used together with ``include``
        :param kwargs: Additional arguments for `dataframe.multi_merge`
        :return: The dataframe resulting from merging the specified pages
        """
        if include is None and exclude is None:
            targets = list(self.keys())
        elif include is not None and exclude is None:
            targets = _klists.list_wrap(include)
        elif include is None and exclude is not None:
            targets = list(set(self.keys()) - set(_klists.list_wrap(exclude)))
        else:
            raise ValueError("Parameters 'include' and 'exclude' are mutually exclusive and cannot be use together")
        aux = [self.get(n) for n in targets]
        return multi_merge(aux, on=on, **kwargs)

    @staticmethod
    def fromkeys(*args):
        dfcoll = DataFrameCollection()
        dfcoll.update(collections.defaultdict.fromkeys(*args, pd.DataFrame()).items())
        return dfcoll


def get_df_rows(df, rindex=None):
    """
    Get the specified rows of a Pandas data frame
    :param df: Pandas dataframe to be scrapped
    :param rindex: Index of the rows to retrieve. It accepts strings and integer numbers. Accepted:
        - None (default): all the rows are retrieved
        - 1: single number, single index
        - 1-4: indexes from 1 to 4, included
        - 2,3,4: indexes 2,3,4
        - 2,3,7-9: combination of the two previous modes
        - head-N: first N rows
        - tail-N: last N rows
        - first: acronym for head-1
        - last: acronym for tail-1
    :return: a list containing one dict per each row (the dict's keys are the column names, its values the row values)
    """
    data = []
    if rindex is None:
        data = []
        for index, row in df.iterrows():
            data.append({k: v for k, v in row.items()})
    elif isinstance(rindex, int):
        data = []
        for index, row in df.iterrows():
            if index == rindex:
                # data.append({k: v for k, v in row.items()})
                return {k: v for k, v in row.items()}
    else:
        rindex = str(rindex)
        if rindex == 'first':
            return get_df_rows(df, df.first_valid_index())
        elif rindex == 'last':
            return get_df_rows(df, df.last_valid_index())
        elif re.fullmatch('head-[0-9]+', rindex):
            rindex = range(df.first_valid_index(), int(rindex.split('-')[1]))
        elif re.fullmatch('tail-[0-9]+', rindex):
            rindex = range(df.last_valid_index() + 1 - int(rindex.split('-')[1]), df.last_valid_index() + 1)
        elif re.fullmatch('[0-9]+-[0-9]+', rindex):
            rindex = range(int(rindex.split('-')[0]), int(rindex.split('-')[1]) + 1)
        elif re.fullmatch('([0-9](-[0-9]+)?,)*[0-9]+(-[0-9]+)?', rindex):
            # rindex = [int(i) for i in rindex.split(',')]
            aux = []
            for i in rindex.split(','):
                try:
                    aux.append(int(i))
                except ValueError:
                    aux.extend(range(int(i.split('-')[0]), int(i.split('-')[1]) + 1))
            rindex = aux
        else:
            raise ValueError("Unexpected value for parameter 'rindex'")

        for index, row in df.iterrows():
            if index in rindex:
                data.append({k: v for k, v in row.items()})
    return data


def df_add_column(dataframe, col, on, how='left') -> pd.DataFrame:
    return dataframe.merge(col, on=on, how=how)


def df_to_excel(output_file, contents: Union[dict, pd.DataFrame]) -> None:
    """
    Saves the contents of a dataframe into an Excel file.

    contents_example = {
        'MasterNmap': df,
        'Metrics_Ports': df_statistics_master,
        'Metrics_Ports_2': df_IPs_StatusPorts,
        'Sum_OpenPorts': df_summary_openports,
        'Sum_ClosedPorts': df_summary_closedports,
        'SumFilteredPorts': df_summary_filteredports
    }
    :param output_file: name for the Excel file
    :param contents: single DataFrame or a dictionary,
        whose keys are page names, and its values the corresponding dataframe
    :return: None
    """
    if isinstance(contents, dict):
        with pd.ExcelWriter(f"{output_file}.xlsx") as writer:
            for sheet_name, dataframe in contents.items():
                dataframe.to_excel(writer, sheet_name=str(sheet_name), index=False, header=True)
    elif isinstance(contents, pd.DataFrame):
        with pd.ExcelWriter(f"{output_file}.xlsx") as writer:
            contents.to_excel(writer, index=False, header=True)
    else:
        raise TypeError("Invalid type for paramterer 'mapping'. Expected: dict|DataFrame")


def multi_merge(dataframes: list, on: Union[str, list], how="inner", **kwargs):
    """
    Merges multiple dataframes sequentially, starting by the first df in the list.

    **Warning**

    If a merged column contains a NaN, all the **integer** values in that column will
    be **cast to float**. NaN is considered a float thus the `dtype`
    of the column is forced to be `float` (https://stackoverflow.com/a/45891250)

    :param dataframes: Set of dataframes to be merged
    :param on: Column to be merged
    :param how: How to do the merge
    :param kwargs: Additional arguments to be passed to panda.merge()
    :return: A new dataframe with all the df from `dataframes` merged
    """
    if not isinstance(dataframes, list):
        raise TypeError("Invalid type for parameter 'dataframes'. Allowed: list")
    elif len(dataframes) < 2:
        raise IndexError("Not enough dataframes to merge. At least 2 dataframes are required")
    else:
        return reduce(lambda left, right: pd.merge(left, right, on=on, how=how, **kwargs), dataframes)


def group_and_count(dataframe, group_by, count_colname='count'):
    """
    Groups and count values in a given DataFrame, generating a new DataFrame with the results

    :param dataframe: (not empty) Dataframe containing the data to be count
    :param group_by: Columns (names) where the group by will be applied
    :param count_colname: New name for the column that contains the count. By default, 'count'
    :return: A new dataframe, with indexes reset to 0, and two columns: The group_by result and the count of each group
    """
    if not isinstance(group_by, list):
        group_by = [group_by]
    return dataframe.groupby(group_by).size().reset_index(name=str(count_colname))


if __name__ == '__main__':
    pass
