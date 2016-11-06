#Motion in Two Dimension without Air Resistance
'''
from math import *
from pylab 

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
title('Motion in Two Dimension')
show()
'''
print("lol")
