def f(x):
    fs=2*x**2+9*x-17
    return fs;

def bisec (a,b,eps):
    if f(b) < 0 and f(a) > 0 or f(a) < 0 and f(b) > 0 :
        c=(a+b)/2.0
        while (b-a)/2.0 > eps:
            if f(c) == 0:
                return c;
            elif f(a)*f(c) < 0:
                b = c
            else:
                a = c
            c=(a+b)/2.0
    return c;

a=0
b=5
eps=10**-6
print bisec(a,b,eps)

from math import *
def f(x):
    return sin(x)*cos(x);

def trap(f,a,b,n):
    h = float(b - a) / n
    s = 0.0
    s += f(a)/2.0
    for i in range(1, n):
        s += f(a + i*h)
    s += f(b)/2.0
    return s * h

a=0
b=1
n=1000
print trap(f,a,b,n)
