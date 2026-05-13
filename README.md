# Indian Stock Portfolio Analysis

## Problem Statement

The objective of this project is to analyze the historical performance of five major Indian stocks:

- RELIANCE
- TCS
- INFY
- HDFCBANK
- ICICIBANK

Using Python and financial data from Yahoo Finance, the project aims to:

- Download historical stock price data
- Compute daily percentage returns
- Analyze correlations between stocks
- Visualize the correlation matrix using a heatmap
- Calculate annualized mean returns and volatility
- Simulate an equal-weighted portfolio
- Compute the portfolio Sharpe Ratio using a 6.5% risk-free rate

The project is designed to build foundational skills in quantitative finance, financial data analysis, portfolio analytics, and data visualization using Python.

---

## What's Been Done So Far

### 1. Data Download
Historical adjusted closing prices for all five stocks are downloaded from Yahoo Finance starting 2020-01-01 using `yfinance`. Rows with missing values are dropped and the data is saved to `data/stock_prices.csv`.

### 2. Daily Returns
Daily percentage returns are computed using `pct_change()` and saved to `data/daily_returns.csv`.

### 3. Correlation Analysis
A correlation matrix is computed from the daily returns and saved to `data/correlation_matrix.csv`. A seaborn heatmap is generated and saved to `outputs/plots/correlation_heatmap.png`.

**Observations:**
- INFY and ICICIBANK are the most correlated pair (0.72), which is a bit surprising since they're in completely different sectors — likely driven by overall market trends.
- RELIANCE and TCS move fairly closely together (0.64), both being large index-heavy stocks.
- Interestingly, the two banking stocks HDFCBANK and ICICIBANK are less correlated with each other (0.37) than INFY is with ICICIBANK.
- All correlations are positive, so this portfolio doesn't offer much sector-level diversification.

---

## Project Structure

```
week1-stock-analysis/
├── portfolio_analysis.py
├── data/
│   ├── stock_prices.csv
│   ├── daily_returns.csv
│   └── correlation_matrix.csv
├── outputs/
│   └── plots/
│       └── correlation_heatmap.png
└── README.md
```

---

## Setup & Usage

### Install dependencies

```bash
pip install numpy pandas matplotlib seaborn yfinance
```

### Run the analysis

```bash
python portfolio_analysis.py
```

All output directories (`data/`, `outputs/plots/`) are created automatically on first run.
