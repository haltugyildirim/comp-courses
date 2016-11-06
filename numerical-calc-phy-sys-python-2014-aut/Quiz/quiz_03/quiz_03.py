#Altug Yildirim
#Quiz 3

from numpy import *
import random

#First Question

def myfactorial(k):
    kfac=0
    for i in range(0,k+1):
        kfac=i*(kfac)
        if kfac == 0:
            kfac=1
    return kfac;

def expoexpa(x,p):
    e_x=0.0
    for k in range(0,p):
        kfac=myfactorial(k)
        e_x=((x**k)/kfac)+e_x
        error=exp(x)-e_x
    return e_x,error;

x=input("Enter the power of exponential: ")
x=x+0.0
n=input("Enter the iteration number: ")
for i in range(1,n+1):
    e_x,error=expoexpa(x,i)
    print "For the iteration number,", i ,"the approximated value is", e_x, "and the error ", error

#Second Question
print "Answer to the second question, now calculating..."
x=0
year=2014
while (x < 100):
    year=year+1
    prob=random.randrange(0,1000000,1)
    long_imp=random.randrange(-180,180,1)
    lat_imp=random.randrange(-90,90,1)
    if prob <= 2000:
        if long_imp > 26 and long_imp < 45:
            if lat_imp > 36 and lat_imp < 42:
                print "Astroid impact in Turkey occur at the year", year, " at Latitude: ", lat_imp, "and Longitude: ", long_imp
                break
