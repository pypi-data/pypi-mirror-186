
import numpy as np
import pandas as pd


def simple_moving_average(data : pd.DataFrame, close_col_index : int, MA_list : list, keep_na=True) -> pd.DataFrame:
    """It calculates the simple moving averages on close prices for a given input list.
    Takes input the OHLCV data, index of closing price and list of moving averages
    returns the dataframe with moving averages columns added."""

    df = data.copy()
    sma_names = ['SMA_'+str(i) for i in MA_list]
    close_col_name = df.columns[close_col_index]

    for i in range(len(MA_list)):
        df[sma_names[i]] = df[close_col_name].rolling(MA_list[i]).mean()

    if not keep_na:
        df.dropna(inplace=True)

    return df