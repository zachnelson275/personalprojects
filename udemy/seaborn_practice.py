import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset('tips')

## Distribution Plots
# print(tips.head())
# sns.distplot(tips['total_bill'], kde = False, bins = 30)
# KDE stands for Kernel Density Estimation
# Basically calculated by summing a normal distribution for every dash on a rug plot

# sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'hex')
# sns.pairplot(tips, hue = 'sex', palette = 'coolwarm')
# sns.rugplot(tips['total_bill'])


## Categorical Plots
# sns.barplot(x = 'sex', y = 'total_bill', data = tips, estimator = np.std)
# Visualize the group by action

# sns.countplot(x = 'sex', data = tips)
# sns.boxplot(x = 'day', y = 'total_bill', data = tips, hue = 'smoker')
# sns.violinplot(x = 'day', y = 'total_bill', data = tips, hue = 'sex', split = True)
# sns.stripplot(x = 'day', y = 'total_bill', data = tips, jitter = True, hue = 'sex')
# sns.swarmplot(x = 'day', y = 'total_bill', data = tips, color = 'black')
# sns.violinplot(x = 'day', y = 'total_bill', data = tips)
# sns.catplot(x = 'day', y = 'total_bill', data = tips, kind = 'violin')


## Matrix Plots

plt.show()