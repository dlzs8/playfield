#!/usr/bin/env python3

import time, random

def sorter(arr):
    n = len(arr)
    for numpass in range(n-1, 0, -1):
        for i in range(numpass): 
            if arr[i] > arr[i+1]:
                r = arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=r


# Creating an array with 1000 random numbers in range from 0 to 1000
lst = []
for i in range(1000):
    lst.append(random.randint(0, 1000))
                
b = time.time()
sorter(lst)
print('Bubble sorter ', time.time() - b)
print(lst)
