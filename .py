# Challenge-Portfolio

import yfinance as yf
import numpy as np
import pandas as pd
import plotly.express as px

from skfolio.preprocessing import prices_to_returns
from skfolio.moments import ShrunkMu, GerberCovariance
from skfolio.prior import EmpiricalPrior
from skfolio.optimization import MeanRisk, ObjectiveFunction
from skfolio.measures import RiskMeasure, RatioMeasure
from skfolio.moments import ShrunkMu, ShrunkMuMethods, GerberCovariance

stocks = ['SPY','TM','JPM','DIS','XOM','GOOG','META','NVDA','HD','CVS','UBER','T','BXSL','GEHC','FAST','LLY','AAPL','BND','PG','JNJ','FICO','MUSA','V']
start = '2017-01-01'
end = '2025-09-02'
prices = yf.download(stocks, start=start, end=end)['Close']

returns = prices_to_returns(prices).dropna()

# Winsorize to remove outlier influence
low, high = 0.01, 0.99
q_lo = returns.quantile(low)
q_hi = returns.quantile(high)
returns_rob = returns.clip(lower=q_lo, upper=q_hi, axis="columns")

mu_est = ShrunkMu(method=ShrunkMuMethods.JAMES_STEIN)
cov_est = GerberCovariance()

prior = EmpiricalPrior(
    mu_estimator=mu_est,
    covariance_estimator=cov_est,
)model = MeanRisk(
    objective_function=ObjectiveFunction.MAXIMIZE_RATIO,
    #ratio_measure=RatioMeasure.SORTINO_RATIO,
    risk_measure=RiskMeasure.SEMI_VARIANCE,
    prior_estimator=prior,
    min_weights=0.0,           # long-only
    max_weights=0.2,           # diversification cap
    l2_coef=0.01,              # weight shrinkage
    budget=1.0,
    portfolio_params=dict(
        name="Max Sortino (robust)",
        min_acceptable_return=0.0,   # MAR in daily terms
        annualized_factor=252,    # daily data
    ),
)

model.fit(returns_rob)

portfolio = model.predict(returns_rob)

print(portfolio.annualized_sharpe_ratio)
print(portfolio.summary())

fig = px.pie( names=stocks, values=model.weights_, title='Interactive Pie Chart', color_discrete_sequence=px.colors.sequential.RdBu )
fig.show()

Stocks = ['SPY','TM','JPM','DIS','XOM','GOOG','META','NVDA','HD','CVS','UBER','T','BXSL','GEHC','FAST','LLY','AAPL','BND','PG','JNJ','FICO','MUSA','V']
Start = '2025-08-04'
End = '2025-09-02'
Prices = yf.download(stocks, start=Start, end=End)['Close'].pct_change().dropna()

Weights = model.weights_
Weights

weighted_returns_portfolio = Prices.dropna().mul(Weights, 
axis = 1)

weighted_returns_portfolio

weighted_returns_portfolio['Portfolio' ] = weighted_returns_portfolio.sum(axis = 1 )
stocks_return = weighted_returns_portfolio['Portfolio' ]


cumulative_returns_portfolio = ((1 + stocks_return).cumprod())
cumulative_returns_portfolio

import matplotlib.pyplot as plt
SP500 = yf.download('^GSPC', start=Start, end=End)['Close'].pct_change().dropna()
SPY = ((1 + SP500).cumprod())
SPY.plot(label = '^GSPC', figsize=(19,8))
plt.ylabel('Returns' )
_ = plt.title('Comparison - Portfolio vs. Benchmark' )
_ = plt.xlabel('Date' )
cumulative_returns_portfolio.plot(label = 'Cumulative Returns of the Portfolio' , 
figsize = (19,8),title = 'Cumulative Returns')
plt.ylabel('Returns' )
_ = plt.title('Comparison - Portfolio vs. Benchmark' )
_ = plt.xlabel('Date' )

portfolio_benchmark = pd.concat([stocks_return, SP500], axis = 1 ).dropna()
portfolio_benchmark.columns = ['Portfolio','Benchmark' ]
portfolio_benchmark

correlation = portfolio_benchmark.corr()
correlation

portfolio_benchmark['RF Rate' ] = 0.00135
portfolio_benchmark['excess' ] = portfolio_benchmark['Portfolio'] - portfolio_benchmark['RF Rate' ]
portfolio_benchmark['excess_b' ] = portfolio_benchmark['Benchmark'] - portfolio_benchmark['RF Rate' ]

sharpe_ratio = portfolio_benchmark['excess'].mean()/portfolio_benchmark['Portfolio' ].std()
sharpe_ratio

import math
annual_days = 252
sharpe_ratio_annual = sharpe_ratio *  math.sqrt(annual_days)
sharpe_ratio_annual

portfolio_benchmark

x = portfolio_benchmark['Portfolio']
y = portfolio_benchmark['Benchmark']
cov_matrix = np.cov(x, y) *252
cov_matrix

market_variance = portfolio_benchmark['Benchmark' ].var() * 252
market_variance

covariance_market = 0.00827424
portfolio_beta = covariance_market / market_variance
portfolio_beta

#Information Ratio and Tracking Error
difference_benchmark_portfolio = portfolio_benchmark['Portfolio'] - portfolio_benchmark['Benchmark' ]
TE = difference_benchmark_portfolio.std()
TE

information_ratio = ((portfolio_benchmark['Portfolio'].mean() - portfolio_benchmark['Benchmark'].mean())/ TE)
information_ratio

alpha = portfolio_benchmark['Portfolio' ].mean() - (portfolio_benchmark['RF Rate' ].mean() + portfolio_beta *(portfolio_benchmark['Portfolio' ].mean() - portfolio_benchmark['RF Rate' ].mean()))
alpha
