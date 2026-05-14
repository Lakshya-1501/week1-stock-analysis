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

## What Was Built

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

### 4. Annualized Returns & Volatility
Per-stock annualized return is computed as `mean daily return × 252` and annualized volatility as `std of daily returns × √252`.

| Stock | Annual Return | Annual Volatility |
|---|---|---|
| RELIANCE | 6.8% | 25.8% |
| TCS | 18.3% | 29.4% |
| INFY | 12.8% | 27.6% |
| HDFCBANK | 15.1% | 28.1% |
| ICICIBANK | 5.8% | 24.1% |

**Observations:**
- TCS has the highest return (18.3%) but comes with the most volatility — classic high risk, high reward.
- ICICIBANK sits at the other end — lowest return (5.8%) but also the steadiest.
- RELIANCE has a surprisingly low return (6.8%) for the largest company in the portfolio.

### 5. Equal-Weighted Portfolio
Each stock gets a 20% weight. Portfolio return is the weighted average of annualized returns, and portfolio volatility is computed from the covariance matrix.

- **Portfolio Return: 11.86%**
- **Portfolio Volatility: 19.8%**

**Observations:**
- The portfolio volatility (19.8%) is lower than every single stock individually (24–29%) — this is diversification working even though all stocks are positively correlated.

### 6. Sharpe Ratio
Computed using a risk-free rate of 6.5% (approximate Indian 10-year bond yield).

- **Sharpe Ratio: 0.27**

**Observations:**
- A Sharpe of 0.27 is quite low — you're getting very little excess return for the risk taken. This is partly because Indian large-caps had a rough stretch and the risk-free rate is relatively high at 6.5%.

### 7. Normalized Price Chart
All stock prices are normalized to 1 on 2020-01-01 so their growth can be compared on the same scale. Saved to `outputs/plots/normalized_prices.png`.

**Observations:**
- INFY was the standout performer, nearly tripling at its peak before pulling back.
- TCS also had a strong run, reaching around 2.5x.
- RELIANCE was the weakest — barely grew compared to the others despite being the largest company.
- All five stocks saw a sharp decline post-2025, visible across the chart.

---

## Project Structure

```
week1-stock-analysis/
├── portfolio_analysis.py
├── portfolio_analysis.ipynb
├── data/
│   ├── stock_prices.csv
│   ├── daily_returns.csv
│   └── correlation_matrix.csv
├── outputs/
│   ├── plots/
│   │   ├── correlation_heatmap.png
│   │   └── normalized_prices.png
│   └── reports/
│       └── portfolio_summary.csv
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

All output directories (`data/`, `outputs/plots/`, `outputs/reports/`) are created automatically on first run.

---

## Author

**Lakshya Garg**

- GitHub: [Lakshya-1501](https://github.com/Lakshya-1501)
- LinkedIn: [lakshyagarg1515](https://www.linkedin.com/in/lakshyagarg1515/)
- Email: garglakshya015@gmail.com
