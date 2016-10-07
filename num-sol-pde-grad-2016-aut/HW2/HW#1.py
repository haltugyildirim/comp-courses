#!/usr/bin/python

from math import sin, exp
from numpy import *

#Fonsksiyonlar

def fsin(x):
	return sin(x)

def fexp(x):
	return exp(x**2)

#Initialization

exact_sin = cos(1)
exact_e = 2*1*exp(1**2)

d = [1e-1,5e-2,1e-2,5e-3,1e-3,5e-4,1e-4,5e-5,1e-5,5e-6,1e-6,5e-7,1e-7]

r_sin=ones((3,size(d)))
r_e=ones((3,size(d))) 

error_sin=ones((3,size(d)))
error_e=ones((3,size(d)))

perror_sin=ones((3,size(d)))
perror_e=ones((3,size(d)))


##Sayisal turevler 

def ileri (f, x, dx):
	return (f(x+dx)-f(x))/dx

def geri (f,x,dx):
	return (f(x) - f(x-dx))/dx

def central (f,x,dx):
	return (f(x+dx)-f(x-dx))/(2*dx)

#####
def op(f, d, r, error,perc_error, exact, x):	
	
	for i in range(size(d)):
		r[0][i]=ileri(f,x,d[i])
		r[1][i]=geri(f,x,d[i])
		r[2][i]=central(f,x,d[i])

		error = abs((exact-r)/r)
		perc_error = error*100
	return r , error, perc_error

###Uygulama

r_sin, error_sin, perror_sin = op(fsin, d, r_sin, error_sin, perror_sin, exact_sin, 1)
r_e, error_e, perror_e = op(fexp, d, r_e, error_e, perror_e, exact_e, 1)

