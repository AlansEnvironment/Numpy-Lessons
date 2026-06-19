import numpy as np

rng = np.random.default_rng(seed = 1) #seed used to reproduce same results

print(rng.integers(1, 7)) #random dice from 1-6, 7 because last number is exclusive (so ur results will be between 1-6)

print(rng.integers(low = 1, high =101, size= (4, 2))) #generates 4 random numbers between 1 and 100, with an array size of 4 x 2

#random floating points
np.random.seed(seed =1)
print(np.random.uniform(low = -1, high = 1, size=3))

#Shuffling an array

rng = np.random.default_rng()
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)

fruits =np.array(["apple", "orange", "banana", "pineapple", "strawberry"])
emojis = np.array(["🍏", "🍊", "🍌", "🍍", "🍓"])
fruit = rng.choice(fruits, size = (3,2)) #using choice function to select a number of fruits of ur choice randomly, can do an array as well
emoji = rng.choice(emojis, size = 3)
print(fruit)
print(emoji)