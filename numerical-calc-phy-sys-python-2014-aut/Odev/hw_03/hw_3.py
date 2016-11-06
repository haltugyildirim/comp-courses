from random import random
from pylab import plot,xlabel,ylabel,title,show
import time

k=input("How many points?")
n=0
k_vec=[]
pi_vec=[]
time_vec=[]
for i in range(1,k+1):
    inside=0
    starttime=time.clock()
    n=10**i
    for j in range(n):
        x,y=random(),random()
        if (x**2+y**2)**(0.5)<1: inside=inside+1
    num_pi=4.0*(float(inside)/n)
    elapsedtime=(time.clock() - starttime)
    k_vec.append(i)
    pi_vec.append(num_pi)
    time_vec.append(elapsedtime)

xlabel('k')
ylabel('pi')
plot(k_vec,pi_vec)
title('Pi versus Iteration Number')
show()

xlabel('k')
ylabel('Time')
plot(k_vec,time_vec)
title('Each Iterations Time versus Iteration Number')
show()


from random import *
sum=1
k=0
while sum!=0 :
    k=k+1
    dice=choice([-4,-3,-1,1,2,4])
    sum=sum+dice
    if k==1:
        sum=sum-1
modw=k%2
if modw == 0:
    print 'Brad Wins!'
else:
    print 'Angelica Wins!'
