import numpy as np

#Summarise data and typically return a single value

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

#print(np.sum(array))
#print(np.mean(array))
#print(np.std(array)) #Standard deviation
#print(np.var(array)) #Variance

#print(np.min(array))
#print(np.max(array))
#print(np.argmin(array)) #position of the minimum value , replace min with max

#Summing all Columns
print(np.sum(array, axis=0)) #axis = 0 all columns (1 by 5 array with sums)
print(np.sum(array, axis = 1)) #axis = 1 all rows (1 by 2 array with sums)


