import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy as spy

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
iris = sns.load_dataset('iris')

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

tc = tips.corr(numeric_only=True)
# sns.heatmap(tc, annot = True, cmap = 'coolwarm')
fp = flights.pivot_table(index = 'month', columns = 'year', values = 'passengers')
# sns.heatmap(fp, cmap = 'magma', linecolor = 'white', linewidth = 3)
# sns.clustermap(fp, cmap = 'coolwarm', standard_scale = 1)
# Clustermap groups like columns and rows together based on similar values


## Grids

# sns.pairplot(iris)
# g = sns.PairGrid(iris)

# g.map_diag(sns.distplot)
# g.map_upper(plt.scatter)
# g.map_lower(sns.kdeplot, cmap = 'cool_d')

g = sns.FacetGrid(tips, col = 'time', row = 'smoker')

g.map(plt.scatter, 'total_bill', 'tip')

plt.show()