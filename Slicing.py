import numpy as np

array = np.array([[1,2,3,4], 
                  [5,6,7,8],
                  [9,10,11,12], 
                  [13,14,15,16]])

#accessing array using subscript operator array[start:end:step], ending index is exclusive | array(rows, columns)


#print(array[0])
#print(array[0:4:2]) #prints out row 0 and row 2

#print(array[::]) #selecting all rows

#print(array[::-1]) #all rows reversed order

#print(array[:,0]) #all rows

#print(array[:, 0:3]) #printing the first three columns

#printing out the even numbers
#print(array[:,1::2])

#print(array[0:2, 0:2]) #first two columns of first two rows



