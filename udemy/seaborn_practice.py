import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
# print(tips.head())
# sns.distplot(tips['total_bill'], kde = False, bins = 30)
# KDE stands for Kernel Density Estimation
# Basically calculated by summing a normal distribution for every dash on a rug plot

# sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'hex')
# sns.pairplot(tips, hue = 'sex', palette = 'coolwarm')
sns.rugplot(tips['total_bill'])

plt.show()