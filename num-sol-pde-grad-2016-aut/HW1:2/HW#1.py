#!/usr/bin/python

from math import sin, exp
from numpy import *
import matplotlib.pyplot as plt

#Fonsksiyonlar

def fsin(x):
	return sin(x)

def fexp(x):
	return exp(x**2)

#Initialization

exact_sin = cos(1)
exact_e = 2*1*exp(1**2)

d = [1e-1,5e-2,1e-2,5e-3,1e-3]

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

#p ler

error_sin= array(([  7.9585,   3.9422,   0.7958,   0.4071,
    9.2541E-2],
 [  7.6068,   3.8497,   0.7773,   0.3886,
    7.4032E-2],
 [  0.1665,   5.5524E-2,   1.8508E-3 ,  1.7608E-4,
    0.9708E-5]))
error_sin=error_sin/100.
error_e= array(([  16.8398,  7.937,   1.5175,   0.7541,
    0.1508],
 [  13.4792,   7.1019,   1.4825,   0.7449,
    0.1489],
 [  1.6793,   0.4175,   1.6554E-2,   3.6788E-3,
    3.6788E-4]))
error_e=error_e/100.

##Plot
x = abs(log(d))
#Sin turevi icin eksenler
y_s = abs(log(error_sin[0]))
y1_s = abs(log(error_sin[1]))
y2_s = abs(log(error_sin[2]))

p_s, z = polyfit(x, y_s, 1)
p1_s, z = polyfit(x, y1_s, 1)
p2_s, z = polyfit(x, y2_s, 1)

plt.figure(1)
plt.subplot(211)
plt.xlabel('log(dx)')
plt.ylabel('log(Error)')
plt.title('sin(x) degisen araliklarda hata')

plt.plot(x,y_s,x,y1_s,x,y2_s)

plt.text(6, 14, 'p_i=%f\np_g=%f\np_m=%f'%(p_s,p1_s,p2_s))

plt.legend(['ileri fark','geri fark','merkezi fark'],loc='best',fontsize=10)

#E fonk

y_e = abs(log(error_e[0]))
y1_e = abs(log(error_e[1]))
y2_e = abs(log(error_e[2]))

p_e, z = polyfit(x, y_e, 1)
p1_e, z = polyfit(x, y1_e, 1)
p2_e, z = polyfit(x, y2_e, 1)

plt.figure(1)
plt.subplot(212)
plt.xlabel('log(dx)')
plt.ylabel('log(Error)')
plt.title('e(x) degisen araliklarda hata')

plt.plot(x,y_e,x,y1_e,x,y2_e)

plt.text(6, 12, 'p_i=%f\np_g=%f\np_m=%f'%(p_e,p1_e,p2_e))

plt.legend(['ileri fark','geri fark','merkezi fark'],loc='best',fontsize=10)
plt.show()
