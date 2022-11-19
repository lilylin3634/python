import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as solver
from functools import reduce

df = pd.read_csv('0050.csv',
                 index_col=0, parse_dates=True)

total_stocks = len(df.columns)

returns = df.pct_change()
returns = returns[1:]
returns.head()

covariance_matrix = returns.cov() * 252
stocks_expected_return = returns.mean() * 252
stocks_weights = np.array([.1, ] * total_stocks)

portfolio_return = sum(stocks_weights * stocks_expected_return)
portfolio_risk = np.sqrt(reduce(np.dot, [stocks_weights, covariance_matrix, stocks_weights.T]))

print('預期報酬率為: ' + str(round(portfolio_return, 4)))
print('風險為: ' + str(round(portfolio_risk, 4)))

risk_list = []
return_list = []
simulations_target = 10 ** 6

for _ in range(simulations_target):
    # random weighted
    weight = np.random.rand(total_stocks)
    weight = weight / sum(weight)

    # calculate result
    ret = sum(stocks_expected_return * weight)
    risk = np.sqrt(reduce(np.dot, [weight, covariance_matrix, weight.T]))

    # record
    return_list.append(ret)
    risk_list.append(risk)

fig = plt.figure(figsize=(10, 6))
fig.suptitle('Stochastic Simulations', fontsize=18, fontweight='bold')

ax = fig.add_subplot()
ax.plot(risk_list, return_list, 'o')
ax.set_title(f'n={simulations_target}', fontsize=16)

fig.savefig('Stochastic_Simulations.png', dpi=300)