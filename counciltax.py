#open a csv file as an array
import numpy as np
import csv
import matplotlib.pyplot as plt
#load the csv file into a numpy array
myarray = np.genfromtxt('counciltax.csv', delimiter=' ')

print (myarray)
print ("shape of the array is", myarray.shape)
print ("size of the array is", myarray.size)
print ("type of the array is", myarray.dtype)
print ("dimension of the array is", myarray.ndim)

#delete the first row and the first column of the array
myarray = np.delete(myarray, 0, 0)
myarray = np.delete(myarray, 0, 1)

print (myarray)
print ("shape of the array is", myarray.shape)
print ("size of the array is", myarray.size)
print ("type of the array is", myarray.dtype)
print ("dimension of the array is", myarray.ndim)
