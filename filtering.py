import numpy as np

#selecting elements from an array given conditions

ages = np.array([[21, 17, 19, 20, 16, 30, 65],
               [39, 22, 15, 99, 18, 20, 21]])

teens = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]
even = ages[ages % 2 ==0 ] #finding even ages
odd = ages[ages %2 !=0] #odd

print(even)
print(adults)
print(teens)
print(seniors)

#PRESERVING THE Orginal SHAPE

adults = np.where(ages >= 18, ages, 0) #where(condition, array, fill value - replace the values that dont match the condition)
print(adults) #get an array with same shape as original(ages) and replacing values that dont meet the condition with 0 (fill value)
#it is slower than boolean indexing (only np.where when you need to preserve the shape of array)




