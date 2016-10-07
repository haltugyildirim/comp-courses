from math import *
import numpy as np
import random

def eigen(A):
    #start guess
    x=np.random.random((len(A),len(A[0])))
    eigenvalue = 0.0
    #loop limit
    K=10
    #tolerance
    tolerance=1* pow(10,-6)
    for k in range(K):
        #calculate eigenvector
        oldx = x
        y = np.dot(A,x)
        x = x / np.linalg.norm(y))
        #calculate eigenvalue
        oldeigenvalue = eigenvalue
        eigenvalue = np.linalg.norm(np.dot(A,x))
        return eigenvalue, eigenvector,x

def eigenval(A,x):
    Ax = np.dot(A,x)
    return np.linalg.norm(Ax)

x = input("Enter the dimension of a symmetric matrix: ")
A=np.random.random((x,x))
print eigen(A)
print eigenval(A,x)
