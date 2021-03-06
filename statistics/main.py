import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
df = pd.read_csv('temperature.csv')

df.plot(kind='bar')


df.plot.kde()

print(stats.kstest('norm', 'norm', N=3))
print(stats.kstest('norm', 'norm', N=500))
print()

print(stats.kstest(df, 'norm', (df.mean(), df.std()), N=len(df)))
plt.show()
