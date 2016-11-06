from math import *
from pylab import *
from numpy import *

def dx(x,y):
    return a*x+b*x*y

def dy(x,y):
    return g*y+d*x*y

a=0.25
b=-0.01
g=-1
d=0.01
x_0=80
y_0=30
t=0.
dt=0.01
i=0
x=[]
y=[]

x.append(x_0)
y.append(y_0)

for i in range(1000):
    t+=dt
    k1_dx=dt*dx(x[i],y[i])
    k2_dx=dt*dx(x[i]+dt/2,y[i]+k1_dx/2)
    k3_dx=dt*dx(x[i]+dt/2,y[i]+k2_dx/2)
    k4_dx=dt*dx(x[i]+dt,y[i]+k2_dx)
    x[i]=x[i]+k1_dx/6+k2_dx/3+k3_dx/3+k4_dx/6
    i+=1

#index krizini asamadik dukkani kapatiyorum hocam...
           __  _
       .-.'  `; `-._  __  _
      (_,         .-:'  `; `-._
    ,'o"(        (_,           )
   (__,-'      ,'o"(            )>
      (       (__,-'            )
       `-'._.--._(             )
          |||  |||`-'._.--._.-'
                     |||  |||
