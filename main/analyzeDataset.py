from multiprocessing.reduction import duplicate
import math
import pandas as pd


class Analysis:

    def __init__(self, data):
        if not isinstance(data, pd.Series):
            raise ValueError("Должно быть pandas Series")
        self.data = data

    def min_num(self):

        return min(self.data)

    def max_num(self):
        return max(self.data)

    def sum_num(self):
        return sum(self.data)

    def duplicate_values(self):
        duplicates = self.data[self.data.duplicated(keep=False)]
        if not duplicates.empty:
            return 0

        return len(duplicates.unique())

    def std_calculate(self):
        std_deviation = self.data.std()

        return  std_deviation

    def sorted_series(self):
        return sorted(self.data)

    def sorted_reversed(self):
        return reversed(sorted(self.data))