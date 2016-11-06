from random import random
all=input("How many points?... ")
inside=0
for i in range(all):
    x,y=random(),random()
    if (x**2+y**2)**(0.5)<1: inside=inside+1
mypi=4.0*(float(inside)/all)
print ("The value of pi for %d points is %f"%(all,mypi))
