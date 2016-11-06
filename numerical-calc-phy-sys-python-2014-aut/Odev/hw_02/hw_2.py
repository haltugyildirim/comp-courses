from pylab import plot,xlabel,ylabel,title,show
from math import radians,sin,cos,exp

v0=input("Enter v0 (m/s): ")
alpha0=input("Enter alpha0 (degrees): ")
m=input("Mass of object: ")
g=input("Gravity: ")
c=input("Drag constant: ")

radalpha0=radians(alpha0)

v_x=v0*cos(radalpha0)
v_y=v0*cos(radalpha0)

x=[]
y=[]
t=0.
dt=0.01
i=0
x_i=0
y_i=0
v_t=(m*g)/c
x.append(x_i)
y.append(y_i)

while y[i]>=0:
    i=i+1
    t=t+dt
#    v_x=v_x-g*(v_x/v_t)*t
#    v_y=v_y-g-g*(v_y/v_t)*t
#    x_i=x_i+v_x*t
#    y_i=y_i+v_y*t
    x_i=x_i+dt*v_x*exp(-g*t/v_t)
    y_i=y_i+dt*v_y*exp(-g*t/v_t)-dt*v_t*(1-exp(-g*t/v_t))
    print x_i
    print y_i
    x.append(x_i)
    y.append(y_i)

xlabel('x')
ylabel('y')
plot(x,y)
title('Motion in two dimensions with air resistance')
show()
#Hocam normalde bunun duzgun calismamasi lazim ama bir sekilde calisiyor
#Ben de size bunu yolluyorum
#  A_A
# (-.-)
#  |-|
# /   \
#|     |   __
#|  || |  |  \__
# \_||_/_/

y[i]=0
while y[i]>=0:
    i=i+1
    t=t+dt
    y_i=y_i-g*t*dt
    x_i=x_i+v_x*dt
    print x_i
    print y_i
    x.append(x_i)
    y.append(y_i)

xlabel('x')
ylabel('y')
plot(x,y)
title('Motion in two dimensions without air resistance')
show()
