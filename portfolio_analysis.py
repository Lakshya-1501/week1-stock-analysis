import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns
import os

# Creating Output Directories
os.makedirs("outputs/plots",exist_ok=True)
os.makedirs("data",exist_ok=True)
os.makedirs("outputs/reports", exist_ok=True)

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

# Sharpe Ratio
risk_free_rate = 0.065

sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility

print("\nSharpe Ratio: ", sharpe_ratio)

# Normalize Price Plot

normalized_prices = data / data.iloc[0]

plt.figure(figsize=(12, 6))

for column in normalized_prices.columns:
    plt.plot(
        normalized_prices.index,
        normalized_prices[column],
        label=column
    )

plt.title("Normalized Stock Prices")
plt.xlabel("Date")
plt.ylabel("Normalized Price")
plt.legend()
plt.grid(True)

# Save figure
plt.savefig(
    "outputs/plots/normalized_prices.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# Summary Report

summary = pd.DataFrame({
    "Metric": [
        "Expected Annual Return",
        "Annual Volatility",
        "Sharpe Ratio"
    ],
    "Value": [
        portfolio_return,
        portfolio_volatility,
        sharpe_ratio
    ]
})

summary.to_csv(
    "outputs/reports/portfolio_summary.csv",
    index=False
)

# Final Results

print("\n================ Portfolio Summary ================")

print(f"Expected Annual Return : {portfolio_return:.2%}")
print(f"Annual Volatility      : {portfolio_volatility:.2%}")
print(f"Sharpe Ratio           : {sharpe_ratio:.2f}")

print("===================================================")