#Motion in Two Dimension without Air Resistance
'''
from math import *
from pylab import *

v0=input("Enter v0 (m/s)...")
alpha0=input("Enter alpha0 (degrees)...")
g=input("Enter g (m/s^2)...")

radalpha0=radians(alpha0)
t_inc=0.01
t=0.
i=0
x=[]
y=[]

x.append(v0*cos(radalpha0)*t)
y.append(v0*sin(radalpha0)*t-0.5*g*t*t)

while y[i]>=0:
    i=i+1
    t=t+t_inc
    x.append(v0*cos(radalpha0)*t)
    y.append(v0*sin(radalpha0)*t-0.5*g*t*t)

xlabel('x')
ylabel('y')
plot(x,y)
title('Motion in two dimensions')
show()
'''

#random module
'''
import random

print "random() :",random.random()
'''

#choice
'''
import random

print "choice a thing from list:", random.choice([1,2,3,5,9])
'''

#randrange range secip o arada aliyor range*start,stop,step)
'''
import random

print "random range from 100 to 1000 with 2 steps:", random.randrange(100, 1000, 2)
'''

#seed([x]) 
'''
import random

print "Random number with seed 10:", random.random()
'''

#shuffle
'''
import random

list = [20,16,10,5];
random.shuffle(list)
print "Reshuffled list :", list
'''

#uniform(x,y) integer yerine aralikta float seciyor
'''
import random

print "Random float from 5 to 10", random.uniform(5,10)
'''

#Random vector & matrices
'''
import numpy
a=numpy.random.rand(3,3)
print a

#or

import numpy as np
a=np.random.rand(3,3)
print a
'''

#Exercise: Finding Pi

from random import *

all=input("How many points to be used for calculation?")

i=0
iceri=0
for i in range(0,all):
    y=random()
    x=random()
    if (x**2+y**2)<=1:iceri=iceri+1

PI=4*(float(iceri)/i)
print "Pi is;", PI

