import numpy as np

# Create a 4D array
arr_4d = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
                   [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]])

print(arr_4d)

# Method 1: Using flatten()
arr_1d_flatten = arr_4d.flatten()

# Method 2: Using ravel()
arr_1d_ravel = arr_4d.ravel()

# Method 3: Using reshape()
arr_1d_reshape = arr_4d.reshape(-1)

print(arr_1d_flatten)
print(arr_1d_ravel)
print(arr_1d_reshape)
