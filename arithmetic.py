import numpy as np

#scalar arithmetics

array = np.array([1.65, 2.03, 3.45])

#print(array +1)
#print(array -2)
#print(array*3)
#print(array /4)
#print(array ** 5)

#VeCTORISED MATH FUNCTIONS
print(np.sqrt(array))
print(np.round(array))

print(np.floor(array)) # always round down
print(np.ceil(array)) #always round up

#Exercise

radii = np.array([1, 3, 6])

print(np.pi* radii**2)

#ELEMENT WISE arithmetics

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 ** array2)
print(array1 / array2)

#Comparison operators

scores = np.array([98, 55, 100, 74, 89, 64])

print(scores == 100) #prints boolean array [False False True False False False]

scores[ scores < 60 ] = 0 #replaces the student with a score less than 60 with a 0 (useful for filtering)

print(scores) 
