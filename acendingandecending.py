# create a numpy array and print in ascending and descending order @pranav version 3.9
import numpy as np

arr = np.array([22, 93, 11, 57, 32, 92, 97])
arr.sort()
print("Ascending order : ", arr)
print("Descending order", arr[::-1])
