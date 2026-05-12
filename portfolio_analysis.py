import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns

# Download Data
tickers = {
    'RELIANCE':'RELIANCE.NS',
    'TCS':      'TCS.NS',
    'INFY':     'INFY.NS',
    'HDFCBANK': 'HDFCBANK.NS',
    'ICICIBANK':'ICICIBANK.NS'
}
data = yf.download(list(tickers.values()),start='2020-01-01',auto_adjust=True,progress=False)['Close']

data.columns = list(tickers.keys())
data = data.dropna()

print(f"Shape: ",data.shape)
print('\n',data.head())


# Compute daily returns
returns = data.pct_change().dropna()
print('\n',returns.head())