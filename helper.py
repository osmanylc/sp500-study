import pandas as pd
import numpy as np

from enum import Enum


class Col(Enum):
    PRICE = 1
    DATE = 2
    DIVIDEND = 3
    EARNINGS = 4
    LOG_RETURNS = 5
    RETURNS = 6


def get_sp500_df(filename):
    sp500_df = (pd
                .read_csv(filename)
                .rename(columns={'Date': Col.DATE.name,
                                 'SP500': Col.PRICE.name,
                                 'Dividend': Col.DIVIDEND.name,
                                 'Earnings': Col.EARNINGS.name})
                [[e.name for e in [Col.DATE, 
                                   Col.PRICE, 
                                   Col.DIVIDEND, 
                                   Col.EARNINGS]]]
                .set_index(Col.DATE.name))
    sp500_df.index = pd.to_datetime(sp500_df.index)
    
    return sp500_df


def get_log_returns(prices_srs):
    """
    Calculate log returns of prices series given.

    :param prices_srs: Series of prices. 
    """
    log_prices_srs = np.log(prices_srs)
    log_returns_srs = (log_prices_srs
                       .diff()
                       .shift(-1)
                       .rename(Col.LOG_RETURNS.name))

    return log_returns_srs

def get_returns(prices_srs):
    """
    Calculates the returns defined as X_i = P_{i+1} / P_i
    """
    returns_srs = ((prices_srs.shift(-1) / prices_srs)
                   .rename(Col.RETURNS.name))
    return returns_srs

def get_pct_dividends(div_srs, price_series):
    """
    Calculates the percent of the price that the dividend 
    paid out represents.
    """
    pct_div_srs = div_srs / prices_srs
    return pct_div_srs

