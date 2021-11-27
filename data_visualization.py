import yfinance as yf
import pandas as pd
import datetime
from datetime import date
import numpy as np
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta
import os

#for-use-function

#grahp colors (rgba 1,1,1 ratio)
colors = [(0.2, 1, 0.2, 1)]


def save_pic(pricegraph):
    plt.savefig('image1'+'.png')
    print('Save Graph')
    return

#declare-basic-function


def delete_graph_pic(files):
    if os.path.exists(files):
        os.remove(files)
        return
    else:
      print(files, "does not exist")


def get_stock_price_history_and_plot_graph(ticker, range, timeframe):
    try:
        thisday = date.today()
        plt.clf()

        if (timeframe.lower() == "y"):

            start = thisday - relativedelta(years=int(range))
            _ticker = yf.download((ticker.lower()), start, thisday)

            pricegraph = _ticker['Adj Close'].plot(color=colors)

        elif(timeframe.lower() == "m"):

            start = thisday - relativedelta(months=int(range))
            _ticker = yf.download((ticker.lower()), start, thisday)

            pricegraph = _ticker['Adj Close'].plot(color=colors)

        elif(timeframe.lower() == "d"):

            start = thisday - relativedelta(days=int(range))
            _ticker = yf.download((ticker.lower()), start, thisday)

            pricegraph = _ticker['Adj Close'].plot(color=colors)

        save_pic(pricegraph)
        return

    except ValueError:
        print('Error Some Shit in Data data_visualization : get_stock_price_history_and_plot_graph')
        return
