import pandas as pd


def clean_series(series, min_val = -10000, max_val = 10000):
    """Быстроя очисткаот цифрового мусора"""
    # Копируем данные
    cleaned = series.copy()

    #Проверяем тип данных
    cleaned = pd.to_numeric(cleaned,errors='coerce')
    non_numeric = cleaned.isna().sum()
    if non_numeric > 0:
        print(f"  Обнаружено {non_numeric} нечисловых значений - удаляю")
        cleaned = cleaned.dropna()

    #Проверяем диапазон
    in_range = ((cleaned >= min_val) & (cleaned <= max_val))
    out_of_range = (~in_range).sum()
    if out_of_range > 0:
        print(f"  Обнаружено {out_of_range} значений вне диапазона [{min_val}, {max_val}] - удаляю")
        cleaned = cleaned[in_range]


    #Преобразуем к целому типу
    cleaned = cleaned.astype('int64')

    return cleaned