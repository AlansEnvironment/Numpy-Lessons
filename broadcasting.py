import numpy as np

#Broadcasting allows NumPy to perform operations on arrays with different shapes by virtually expanding dimensions 
#So they match the larger array's shape

#Dimensions have the same size
#Or
#Dimensions has a size of 1

array1 = np.array([[1,2,3,4]]) #both are 2D arrays 1 row 4 columns 
array2 = np.array([[1],[2],[3],[4]]) #1 column 4 rows

print(array1.shape)
print(array2.shape)

print(array1*array2) #resulting in a 4*4 array
print("\n")
array3 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])
print(array3.shape)
print(array2.shape)

print(array3*array2)


numbers = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
multiply_by = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(numbers.shape)
print(multiply_by.shape)
print(numbers*multiply_by) #10 by 10 array

