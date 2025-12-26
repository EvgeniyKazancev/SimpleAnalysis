import pandas as pd
import matplotlib.pyplot as plt

def create_df(series):
    return pd.DataFrame({'Исходные значения': series.values,
                         'По возрастанию': sorted(series.values),
                         'По убыванию': sorted(series.values, reverse = True)})

