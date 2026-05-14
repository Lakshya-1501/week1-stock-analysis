import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns
import os

# Creating Output Directories
os.makedirs("outputs/plots",exist_ok=True)
os.makedirs("data",exist_ok=True)

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
print('\nStocks Data:')
print(data.head())

data.to_csv("data/stock_prices.csv")


# Compute daily returns
returns = data.pct_change().dropna()
print('\nDaily Returns:')
print(returns.head())

returns.to_csv("data/daily_returns.csv")

# Correlation Heatmap
corr_matrix = returns.corr()

corr_matrix.to_csv("data/correlation_matrix.csv")

print("\nCorrelation Matrix:")
print(corr_matrix)

plt.figure(figsize=(12,6))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    linewidths=0.5
)

plt.title("Stock Return Correlation Heatmap")

plt.savefig(
    "outputs/plots/correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# Annualized returns
annual_returns = returns.mean() * 252    # 252 trading days

print("\nAnnual Returns:")
print(annual_returns)

# Annualized volatility
annual_volatility = returns.std() * np.sqrt(252)

print("\nAnnual Volatility:")
print(annual_volatility)

# Portfolio Weights
num_stocks = len(tickers)

weights = np.array([1/num_stocks]*num_stocks)

# Portfolio Returns
portfolio_return = np.dot(weights,annual_returns)
print("\nPortfolio return: ",portfolio_return)

# Portfolio Volatility
cov_matrix = returns.cov() * 252

portfolio_variance = np.dot(
    weights.T,
    np.dot(cov_matrix,weights)
)

portfolio_volatility = np.sqrt(portfolio_variance)
print("\nPortfolio Volatility: ",portfolio_volatility)