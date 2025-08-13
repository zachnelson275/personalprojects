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

df[(df['W'] > 0) & (df['Y'] > 1)] # Multiple conditions using and
df[(df['W'] > 0) | (df['Y'] > 1)] # Multiple conditions using or
# (df['W'] > 0) | (df['Y'] > 1) 
# This is a series of bool values, which can be passed
# into the original data frame to get all rows where either
# condition evaluates to true

df.reset_index() # Resets index of the data frame
# Useful for turning the index into a column
# Only happens in place, doesn't change the original data frame
print(df)

newind = 'CA NY WY OR TX'.split()
df['States'] = newind
df.set_index('States', inplace=True) # Set index to a specific column
# All pandas edits need to have the parameter inplace set to True for it to 
# apply to the data frame. Use regular methods without inplace to test output
# before applying the changes
print(df)

# Index Levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = p.MultiIndex.from_tuples(hier_index)

dfd = p.DataFrame(randn(6,2), hier_index, ['A', 'B'])
dfd.loc['G1'] # Returns sub dataframe of subindex G1
dfd.loc['G1'].loc[2] # Returns row 2 of subindex G1
dfd.index.names = ['Groups', 'Num'] # Set names of index levels
print(dfd)

dfd.loc['G2'].loc[2]['B'] 
# Returns value of column B, row 2, subindex G2
# dfd.xs('1', level = 'Num') 
# Cross section method to return all values of 1 at level Num

d = {'a':[1, 2, np.nan], 'b':[5, np.nan, np.nan], 'c':[1, 2, 3]}
dft = p.DataFrame(d)
print(dft)
print(dft.dropna(axis = 1)) # Drops columns with any null values
print(dft.dropna(thresh = 2))  # Drops rows with 2 or more non-null values
print(dft.dropna(subset = ['a'])) # Drops rows where column a has null values

print(dft.fillna('FILL VALUE')) # Fills null values with parameter
print(dft['a'].fillna(value=dft['a'].mean())) # Fills null values with mean of column A

### Group By ###
data = {'Company':['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales':[200, 120, 340, 124, 243, 350]}
dfg = p.DataFrame(data)
byComp = dfg.groupby('Company') # Returns a groupby object
byComp.mean(numeric_only=True) # Returns mean of each group


byComp.sum(numeric_only=True).loc['FB'] # Returns sum of FB group
byComp.describe() # Returns descriptive statistics of each group
byComp.describe().transpose() # Transpose the output for better readability
byComp.describe().transpose()['FB'] # Returns descriptive statistics of FB group

### Concatenation ###
df1 = p.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 'B' : ['B0', 'B1', 'B2', 'B3'], 'C' : ['C0', 'C1', 'C2', 'C3'], 'D' : ['D0', 'D1', 'D2', 'D3']}, index = [0, 1, 2, 3])
df2 = p.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'], 'B' : ['B4', 'B5', 'B6', 'B7'], 'C' : ['C4', 'C5', 'C6', 'C7'], 'D' : ['D4', 'D5', 'D6', 'D7']}, index = [4, 5, 6, 7])
df3 = p.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'], 'B' : ['B8', 'B9', 'B10', 'B11'], 'C' : ['C8', 'C9', 'C10', 'C11'], 'D' : ['D8', 'D9', 'D10', 'D11']}, index = [8, 9, 10, 11])
print(p.concat([df1, df2, df3])) # By default, concat joins the rows together vertically
print(p.concat([df1, df2, df3], axis=1)) # Concatenates the dataframes horizontally. This case results in a 12x12 data frame

left = p.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'], 'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3']})
right = p.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'], 'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']})
merged = p.merge(left, right, how='inner', on='key') # Inner is default merge method
print(merged)

# Join is the same thing as merge, except it uses the index rather than a key column