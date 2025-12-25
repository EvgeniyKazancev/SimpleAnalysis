import pandas as pd
import numpy as np

def save_series():
    """Функция генерации случайных  данных и создание обьекта Series.
     Возвращает: обьект Series с 1000 случайных целых чисел"""
    series = pd.Series(np.random.randint(-10000, 10000, 1000))

    # Сохранение данных в csv файл для дальнейшего использования
    #series.to_csv('generate_series.csv', header=['Значения'])
    return series



