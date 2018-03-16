##https://www.hackerrank.com/challenges/time-series-prediction/problem
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd

my_data = pd.read_csv("timeseries_prediction_data.csv")
n=500
offset = 7
last = 130
X = []
for t in range(n - last, n):
    z = [t]
    z.extend([1 if w == t % offset else 0 for w in range(offset)])
    X.append(z)
	
Y=my_data[-(last+30):-(30)]['x1'].values
r = sm.OLS(Y, X).fit()

X = []
for t in range(30):
    z = [n + t]
    z.extend([1 if w == (n + t) % offset else 0 for w in range(offset)])
    X.append(z)
ans = r.predict(X)

fig, ax = plt.subplots()
ax.plot(list(range(1,31)), my_data[-30:]['x1'], 'r-', label="original")
ax.plot(list(range(1,31)), ans, 'b-', label="predicted")
ax.legend(loc="best");