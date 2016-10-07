import numpy
import random

#generate a 2000x4 matrix A

M= numpy.random.random((2000,4))

#find M(dagger)*M

M_dag = M.conj().transpose()

C=numpy.dot(M_dag, M)
print C

#Matlab Eig//linalg

e_value, e_vector = numpy.linalg.eig(C)
print e_value, e_vector

#Jacobi Rotation

import random
import numpy as np
from math import *

x = input("Enter the dimension of a symmetric matrix: ")
A=np.random.random((x,x))
q=1
p=0
t=(A[q,q]-A[p,p])/(2*A[p,q])
c=cos(t)
s=sin(t)
P=np.identity(x-1)

for p in range(x-1):
    for q in range(x-1):
        if p != q:
            P[q,q]=c
            P[p,p]=c
            P[p,q]=s
            P[q,p]=-s
            P_dag=np.matrix.H(P)
            D=dot(P_dag,A)
            D=dot(D,P)
print D

#Power Method

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

#calculate real value in order to control if out method is working
def eigenval(A,x):
    Ax = np.dot(A,x)
    return np.linalg.norm(Ax)

x = input("Enter the dimension of a symmetric matrix: ")
A=np.random.random((x,x))
print eigen(A)
print eigenval(A,x)
