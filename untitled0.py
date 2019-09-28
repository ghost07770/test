# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:04:50 2019

@author: Kritartha Patowary
"""
import numpy as np
'''
arr = np.array([[1,2,3], [4,2,5]])

print("Array is of type:",type(arr))
print("No. of dimensions:",arr.ndim)
print("Shape of array:",arr.shape)
print("Size of the array:",arr.size)
print("Array stores elements of type",arr.dtype) '''

arr = np.array([1,2,3])
print("Array with rank 1:\n",arr)

arr = np.array([[1,2,3],[4,5,6]])
print("Array with rank 2:\n",arr)

arr=np.array((1,2,3))
print("\nArray created using passed tuple:",arr)

arr = np.array([[-1,2,0,4],
                [4,-0.5,6,0],
                [2.6,0,7,8],
                [3,-7,4,2.0]])
print("Initial array:",arr)

sliced_arr = arr[:2, ::2]
print("Array with first two rows and alternating columns(0 and 2)",sliced_arr)

index_arr = arr[[1,1,0,3],[3,2,1,0]]
print(index_arr)

a=np.array([[1,2],[3,4]])
b=np.array([[5,5]])
print(a+b)