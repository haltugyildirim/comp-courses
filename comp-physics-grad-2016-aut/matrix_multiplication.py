#############################################
#    First class of computational physics   #
#    Matrix multiplication                  #
#    Lecturer: Nazmi Postacioglu            #
#    Created by haltugyildirim              #
#############################################

from math import *
from time import time
import numpy as np
#adding a function(function can be added anywhere)
def matrix_product(A,B, time_=0):
    c=np.zeros(A.shape, 'float')
    bb=B.transpose()
    t1=time()
    for k1 in range(c.shape[0]):
        for k2 in range(c.shape[1]):
            c[k1][k2] =c[k1][k2]+(A[k1]*bb[k2]).sum()
    t2=time()
    if(time_>0):
        print "time from function=", t2-t1
    return c

#matrix multiplication manually

dim=100
#a=np.ones((2,2),float) #this is an ones matrix
a=np.random.random((dim,dim))
#print cos(pi) #just for showing
#print np.cos(a) #just for showing
#b=a+8. if b=a #then this will totally equals two matrices
b=np.array(a)
a[0][0]=10

#print b
b[1]=b[1]+b[0]
#print b
c=np.zeros(a.shape, 'float')
bb=b.transpose()
t1=time()
for k1 in range(c.shape[0]):
    for k2 in range(c.shape[1]):
        #for k3 in range(a.shape[1]): #These two line are not using the sum function thus
            #c[k1][k2] =c[k1][k2]+a[k1][k3]*b[k3][k2] #takes more time(4sec approx.) than with sum(0.2 approx.)
            c[k1][k2] =c[k1][k2]+(a[k1]*bb[k2]).sum()
t2=time()
#print c[0][0]
print c[20][30],"  ",t2-t1,"sum function multiplication"
t1=time()
c=np.dot(a,b)
t2=time()
print c[20][30],"  ",t2-t1,"dot product ready function"

#dot product
t1=time()
c=np.matrix(a)*np.matrix(b)
t2=time()
print c[20,30],"  ",t2-t1,"np.matrix multiplication"
product=matrix_product(a,b)
print product
