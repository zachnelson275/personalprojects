# import numpy as np 
# arr = np.arange(0, 11)
# arr[:] = 0
# print(arr)

# arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
# print(arr_2d)
# # arr_2d[row_i][column_i]
# # arr_2d[1][2] = 30
# # arr_2d[row_i, column_i]
# # arr_2d[2, 1] = 40
# # arr_2d[:2, 1:] = [10, 15],
# #                  [25, 30]

# arr = np.arange(1,11)
# arr_4 = arr > 4 # boolean array
# print(arr_4)
# print(arr[arr_4])

# print(arr_2d[arr_2d <= 30])
# # masked_arr_2d = np.where(arr_2d < 30, arr_2d, )
# # print(masked_arr_2d)

# arr_20 = np.arange(0, 20)
# print(arr_20 / 20)

# print(np.sum(arr_20))
# print(np.std(arr_20))

# # print column totals
# print(arr_2d.sum(axis = 0))
# # print row totals
# print(arr_2d.sum(axis = 1))

# i5 = np.eye(5)
# print(i5)