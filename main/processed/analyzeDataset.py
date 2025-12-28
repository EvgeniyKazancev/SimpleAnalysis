
import pandas as pd


class Analysis:
    """Класс анализа данных из обьекта Series"""
    def __init__(self, data):
        if not isinstance(data, pd.Series):
            raise ValueError("Должно быть pandas Series")
        self.data = data
    # Находим минимальное значение
    def min_num(self):

        return min(self.data)

    # Находим максимальное значение
    def max_num(self):
        return max(self.data)

    # Находим минимальное значение
    def sum_num(self):
        return sum(self.data)

    # Находим количество повторяющихся элементов
    def duplicate_values(self):
        value_counts = self.data.value_counts()
        duplicates = value_counts[value_counts > 1]


        return len(duplicates)
     # Вычисление среднеквадратического отклонения
    def std_calculate(self):
        std_deviation = self.data.std()

        return  std_deviation

