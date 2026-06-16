import numpy as np

array = np.array([[['A', 'B', 'C'], ['E', 'F', 'G'], ['H', 'I', 'J']], #layer 1 [0]
                  [['K', 'L', 'M'], ['N', 'O', 'P'], ['Q', 'R', 'S']], #layer 2 [1]
                  [['T', 'U', 'V'], ['W', 'X', 'Y'], ['Z', '_', '__']]]) #layer 3 [2]

#making a 3D array (i'm aware i forgot 'D')

#print(array.ndim) #3
#print (array.shape) #(3,3,3) - Depth, Rows, Columns

#print(array[0][0][0]) #chain indexing 
#print(array[0,0,1]) #B

###EXERCISE#####

word = array[1,1,2] + array[1,0,1] + array[2,0,1] + array[0,2,0] #PLUH
print(f'\nThe word is: {word}\n')


