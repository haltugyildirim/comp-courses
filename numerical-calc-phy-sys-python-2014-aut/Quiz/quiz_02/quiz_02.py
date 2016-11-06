#Altug Yildirim
#First Problem of the Quiz 2:
#In the main program:
#Ask the user to enter two numbers (x and y). (These numbers
#are two sides of a right triangle other than the hypotenuse.)
#If x or y is zero or negative, print "No triangle" to the screen.
#If x and y are nonzero or positive, call a function that finds the
#hypotenuse of this triangle if x and y are nonzero and positive.
#Print the result on the screen.
#In the function:
#The inputs are two numbers x and y.
#The output is the hypotenuse of the triangle.


print "Finding Hypotenuse of a Triangle"
x=input ("Enter first of the sides of the triangle: ")
y=input ("Enter second of the sides of the triangle: ")

def hypo(i,j):
    h=(i**2+j**2)**0.5
    return h

if x <= 0 and y <= 0:
    print "No Triangle"
else:
    print "Answer for the First Exercise;", hypo(x,y)

#Second Problem of Quiz 2:

from numpy import *
print "Finding the smallest and biggest values in a matrix:"

def minmaxvector(mv):
    x1=mv[0].max()
    x2=mv[1].max()
    x3=mv[2].max()
    a=array([x1,x2,x3])

    y1=mv[0].min()
    y2=mv[1].min()
    y3=mv[2].min()
    b=array([y1,y2,y3])
    return a,b;

def maxminofall(m1,m2):
    x1=m1.max()
    y1=m2.min()
    return x1,y1;

m=zeros((3,3))
for i in range(3):
    for j in range(3):
        m[i,j]=input("Input the matrix element: ")
        print m
mone,mtwo = minmaxvector(m)
x1,y1=maxminofall(mone,mtwo)
print x1,y1
