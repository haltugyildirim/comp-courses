from numpy import *
import time
start = time.clock()
a=array([[1.,2.,3.],[4.,5.,6.]])
b=a.T
c=dot(a,b)
print 'Matrix [a]'
print a
print 'Matrix [b]'
print b
print 'Matrix [c] = [a] x [b]'
print c
print 'Code took ', time.clock() - start, ' seconds'
#####################
######Sources########
#https://stackoverflow.com/questions/14452145/ -->
#--> how-to-measure-time-taken-between-lines-of -->
#--> -code-in-python
