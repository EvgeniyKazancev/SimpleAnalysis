import pandas as pd


def create_df(series):
    return pd.DataFrame({'Исходные значения': series.values,
                         'По возрастанию': sorted(series.values),
                         'По убыванию': sorted(series.values, reverse = True)})