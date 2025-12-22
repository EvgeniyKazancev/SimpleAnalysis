import pandas as pd
import matplotlib.pyplot as plt
import create_dataframe
import numpy as np
from matplotlib.lines import lineStyles


def line_graf(series):

    plt.plot(series,marker = '.',color = 'r', linestyle = '-')
    plt.title("Линейный график")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)

def histogram(series):

    new_series = (series / 100).round() * 100

    plt.hist(new_series, bins=5, color='y', edgecolor='black')
    plt.title("Гистограмма")
    plt.xlabel("Значения")
    plt.ylabel("Частота")


def graf(series):
    sort_series = sorted(series.values)
    revers_sort_series = sorted(series.values,reverse=True)


    plt.plot(sort_series, marker='.', color='r', linestyle='-')
    plt.plot(revers_sort_series, marker='.', color='g', linestyle='-')

    plt.plot(sort_series, marker='.', color='r', linestyle='-',
             label='По возрастанию ')
    plt.plot(revers_sort_series, marker='.', color='gray', linestyle='-',
             label='По убыванию ')
    plt.xlabel('Длина')
    plt.ylabel('Значения')
    plt.grid(True)
    plt.legend()

def separate_win(series):
    plt.figure(1)
    line_graf(series)

    plt.figure(2)
    histogram(series)

    plt.figure(3)
    graf(series)

    plt.show()



