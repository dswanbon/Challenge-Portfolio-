Hypothesis: 

None of the other competitors will be able to develop an actively managed trading strategy that beats a sound passive portfolio consistently. Therefore, I constructed a passive portfolio based on maximizing the Sortino Ratio using robust statistics. 

Research Process: 

I had read about the Sortino Ratio prior to participating in the trading competition. One of the many criticisms of the mean-variance optimal portfolio is that it maximizes the Sharpe Ratio, which relies on standard deviation and variance. Both of those measures penalizes upward volatility, which investors should reward because that quality can result in higher returns. The Sortino Ratio only looks at downward volatility, and uses semideviation and semivariance instead of standard deviation and variance. A textbook I read claims that practitioners favor the Sortino method over other models. So I gave it a try. 

To select the stocks I invested in I made sure to draw from different industries to make sure the portfolio is not overly susceptible to declines in one or a few parts of the economy. Additionally, I created a heatmap to observe correlations between all 23 of the stocks I defined as the investable universe. 

A common criticism of using academic portfolio theory to construct real portfolios is that such models are often very sensitive to data inputs. I mitigated this problem by winsorizing my stock returns prior to performing optimization to remove outlier declines and increases, which helps capture the true tendency of each asset. Additionally, I drew from robust statistics when estimating expected returns and return covariances. Specifically, I used the James Stein shrunk mean method, and the Gerber covariance estimator to determine my inputs. 

The final step in my data-cleaning process was to set maximum and minimum weights to ensure my model outputs a well diversified portfolio. Sometimes optimal portfolio models can recommend extreme weights and omit assets, which is contrary to the objective of diversification. My minimum weight was zero, and my maximum was 20%.

Data Sources: 

All of my stock return data comes from Yahoo Finance. 

Backtesting: 

Choosing a period to perform optimization requires some judgement. Going too far back risks using data that does not reflect present market realities accurately. I decided to use an eight year time span for my data, which extends three years before the Covid pandemic, which is an anomalous time period, but has more years after that event that can provide reliable insight into the behavior of each stock post-pandemic, especially after applying robust statistics to the returns. 

While backtesting was not integral to my process, I did set up a backtesting program to see how my portfolio strategy would have performed over different holding periods. An issue with backtesting this particular portfolio is that at least one of the instruments it includes was created or added to Yahoo Finance very recently, so backtests before 08/04/23 are not possible without excluding that asset. Below I provide a backtest of what holding my portfolio from August 4th 2023 to August 29th 2025 would entail: 


In blue is the S&P 500, and in orange is my optimal portfolio. My model outperforms the market, but closely matches its behavior. 

Optimization: 

Besides rebalancing the weights of each asset twice a week, little had to be done once the initial model was created. The rebalancing process also ensures that I buy losers and sell winners, since when a stock goes up, it takes up a greater percentage of my portfolio, while the opposite is true of losers which become a smaller portion of my portfolio. Since stocks are somewhat mean reverting in the short run, this process is mathematically intuitive and agrees with my prior reading on applied portfolio management. 

I’ll also provide a quick mathematical explanation of how portfolio optimization using the Sortino ratio works, in a two asset world. 

Suppose there are two assets, that can provide the following four returns with equal probability:

Asset 1: 0.1, 0.04, -0.02, -0.08                                 Asset 2: 0.06, 0.03, 0.01, -0.01

Computing the Expected Returns for each asset gives: 

Asset 1: 0.01         Asset 2: 0.0225

In order to perform optimization with the Sortino Ratio, we must define a minimum acceptable return or MAR, in this case 0.01. 

The portfolio return can be defined as W*R1+(1-W)*R2 = Rp

The Sortino Ratio is: (ERp-MAR)/ Downside Deviation

Downside Deviation(w)=(s∑​ps​⋅min(0,Rps​(w)−MAR)^2)^0.5

Next we would have to compute the downside deviation for all eight returns, and compare Sortino Ratios to find the optimal allocation. Optimization cannot be performed very easily because the objective function is non-differentiable and non-convex, which means that numerical methods are required to solve the problem. 

Integration with Limex API: I did not use the API. I created an Excel spreadsheet and using the optimal portfolio weights from my python file and price data I determined how much money I would allocate to a given stock. 

Validation: 

I calculated the beta of my portfolio as about 0.89 in Excel using five year stock betas provided on Yahoo Finance, which means that my portfolio is somewhat insensitive to movements in the S&P 500. Anecdotally, I noticed that when the market was slightly down, my Sharpe Ratio lead was generally high. 

During the final week of the competition I became interested in my portfolio’s alpha and tracking error, because I started to wonder how closely my portfolio allocation matches the S&P 500. I also wanted to determine if my model exemplified active or passive management. Using data starting from 08/04/25 to 8/29/25, or the duration of the competition, I computed the following portfolio statistics. 

Beta: 0.91

Tracking Error: 0.0026

Information Ratio: 0.2097

Alpha:  2.49

The risk free rate I assume for the relevant calculations is 0.00135, which gives approximately what the Limex site listed my Sharpe Ratio as being. 

Based on the portfolio statistics presented above, it would appear that my portfolio is insensitive to market movements, and differs little from the market in asset composition. The information ratio suggests that the portfolio does somewhat beat the market consistently. The very positive Alpha further confirms that this portfolio beat the market over the chosen time period. 

Improvements: 

While I consider this to be a solid portfolio strategy, I can propose some ways it could be enhanced. I only invested in American stocks, which limits diversification in two distinct ways. Only investing in U.S. companies forfeits the diversification benefits that can be achieved from investing internationally. Additionally, there is only one non-stock asset that I invested in, namely the Vanguard bond index. With expanded access to more asset classes, this portfolio could be more diversified. However there is at least one academic paper that recommends an all stock portfolio, so the asset allocation choice may actually be defensible. 

Studies have also shown that diversification benefits persist beyond 20 assets, so if I invested into more securities this effect could have been amplified further. I also saved about 10k-14k in case of emergency, but there was never any emergency or need to actively manage throughout the competition. I could have generated more equity had I invested all of the 100k. 

Conclusion:

I conclude that I successfully created a passive portfolio that generally beats the market. My portfolio also reacts somewhat weakly to movements in the S&P 500, and illustrates that optimal portfolio models can be a viable investment strategy when complemented by robust statistics and weight restrictions that resemble what I used for my model. I also find that the Sortino ratio functions well as a quantitative model. Additionally I highlight some areas of improvement for my model that could further boost its Sharpe ratio. 





