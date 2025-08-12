import numpy as np
import pandas as p

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}
series = p.Series(my_data, labels)
# Output
# a    10
# b    20
# c    30
series2 = p.Series(arr)
# Output
# 0    10
# 1    20
# 2    30
series3 = p.Series(d)
# Output
# a    10
# b    20
# c    30

ser4 = p.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])
# Output
# USA        1
# Germany    2
# Italy      5
# Japan      4

ser5 = p.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])

print(ser4 + ser5)
print(ser5 + ser4)

from numpy.random import randn
np.random.seed(101)
df = p.DataFrame(randn(5,4),['A','B','C','D','E'], ['W','X','Y','Z'])
print(df)
df['new'] = df['W'] + df['Y']
print(df)
df.drop('new', axis = 1, inplace = True)
# df = df.drop('E')
print(df)

df['W'] # Grab a column
df.loc['C'] # Grab a row by name
df.iloc[2] # Grab a row by index

df.loc['B','Y'] # Grab an item, row,column
df.loc[['A', 'B'], ['W', 'Y']] # Grab multiple items by range

booldf = df > 0 # Returns bool data frame
# df[booldf] == df[df>0]

df['W'] > 0 # Returns series of bool values
df[df['W'] > 0] # Returns data frame where bool values = True
# In this case, returns all items from rows A, B, D, and E
# This is because df['W'] > 0 filters out all items in column W that are less than 0
# which is just row C. Then, passing that series into the original data frame
# returns all rows except C
# Column conditionals return a series values, which can be combined with row
# conditionals to filter data even more

print(df[df['W'] > 0][['X', 'Y']])