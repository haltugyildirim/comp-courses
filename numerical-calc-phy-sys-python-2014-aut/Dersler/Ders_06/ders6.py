#Matrix Operations

#Use numpy
'''
import numpy
import numpy as np
from numpy import *
'''
'''
import numpy as np
a=np.array([1,2,5,8], float)
print a
print type(a)
print a[:2]
print a[3]
'''

import numpy as np
'''
a=np.array([[1,2,3],[4,5,6]], float)
print a
print a[0,0]
print a[0,1]
print a[1,:]
print a[:,2] #ikinci sutunu almak icin
print a.shape
print a.dtype
print len(a)
print 90 in a
'''

'''
a=np.array(range(10), float)
print a
a = a.reshape((5,2))
print a
'''
'''
a = np.array([1,2,3], float)
b=a
c=a.copy()
a[0] = 0
print a
print b
print c

a.tolist()
print list(a)
print b
'''
'''
a=np.array([1,2,3],float)
print a
a.fill(0)
print a
'''
'''
a=np.array(range(6), float).reshape((2,3))
print a
b=a.transpose()
print b
'''
'''
#parallel islemcili pcler matrisleri vektor olarak isler o yuzden vektore ceviririz vs
a=np.array([[1,2,3],[4,5,6]], float)
print a
print a.flatten()
'''

'''
a=np.array([1,2,3,])
print a
print a[:,np.newaxis]
print a[:,np.newaxis].shape

print np.arange(5, dtype=float)
print np.arange(1,6,2, dtype=int)
print np.arange(1,6,0.5, dtype=float)
'''

'''
a=np.array([[1,2,3],[4,5,6]],float)
print np.zeros_like(a)
print np.ones_like(a)
print np.identity(4, dtype=float)
print np.eye(4, k=1, dtype=float)
'''

'''
a=np.array([1,2,3],float)
b=np.array([4,5,6],float)
print a+b
print a % b
'''

'''
a=np.array([1,2,9],float)
print np.sqrt(a)

#yuvarlama
a=np.array([1.1,1.5,1.9],float)
print 
'''

a=np.array([1,4,5],int)
for x in a:
    print x
