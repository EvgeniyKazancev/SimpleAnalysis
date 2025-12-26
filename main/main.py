from processed import analyzeDataset, randomData, create_dataframe
from visual.visual import separate_win


def main():
   # randomData.save_series()
   # data = pd.read_csv('generate_series.csv', index_col=0).squeeze()

    series = randomData.save_series()
    analysis = analyzeDataset.Analysis(series)

    print("=" * 50)
    print("                 Анализ DataSet")
    print("=" * 50)
    print("Минимальное значение:", analysis.min_num())
    print("Максимальное значение:", analysis.max_num())
    print("Сумма всех чисел: ", analysis.sum_num())
    print("Количество повторяющихся значений: ", analysis.duplicate_values())
    print("Среднеквадратическое отклонение: %.2f" % analysis.std_calculate())


    create_dataframe.create_df(series)

    separate_win(series)


if __name__ == "__main__":
    main()
