import pandas as pd
import matplotlib.pyplot as plt
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
    plt.show()

def separate_win(series):
    plt.figure(1)
    line_graf(series)

    plt.figure(2)
    histogram(series)


    plt.show()