#Functions
'''
def functionname(parameters):
    "function_comment"
    function_suite
    return [expression]
'''

#defining functions
'''
def printme(str):
    "This prints a passed string into this function"
    print str
    return

#Now you can call printme function
printme("I'm first call to user defined function!");
'''

'''
#Function definition is here
def changeme (mylist):
    "This changes a passed list into this function"
    mylist = [1,2,3,4]; #This would assign new reference in mylist
    print "Values inside the function:", mylist
    return

#Now you can call changeme function
mylist = [10,20,30];
changeme(mylist);
print "Values outside the functions:", mylist
'''

'''
#Function definition again
def printinfo(name, age):
    print "Name:", name
    print "Age:", age
    return;

#Now you can call printinfo without bothering about order of inputs
printinfo(age=50, name="miki");
'''

'''
#If there is no input
def printinfo(name, age=35):
    "This prints a passed info into this function"
    print "Name: ", name;
    print "Age: ", age;
    return;

#Now you can call printinfo function
printinfo(age=50, name="miki");
printinfo(name="miki");
'''

'''
#Add Function
def sum(arg1, arg2):
    total = arg1 + arg2
    print "Inside the function: ", total
    return total;

#calling sum function
total = sum(10,20);
print "Outside the function:", total
'''

'''
#Global variable
total = 0; #This is global variable
#Func def
def sum(arg1, arg2):
    total = arg1 + arg2;
    print "Inside the function local total:", total
    return total;

#Now you can call sum function
sum(10,20)
print "Outside the function global total:", total
'''

'''
#numpy arrayla func
from numpy import *

def sum(mat1,mat2):
    #Add two matrices
    mat3=mat1+mat2
    return mat3;

m1=array([[1,2],[3,4]])
m2=array([[4,3],[2,1]])
print sum(m1,m2)
'''

'''
#numpy matrisi degil, piton matrisi
def sum(mat1,mat2):
    mat3=mat1+mat2
    return mat3;

m1=[[1,2],[3,4]]
m2=[[4,3],[2,1]]
print sum(m1,m2)
#toplama yapmiyor!!11!1
'''

'''
#Exercise_1
def hypo(x,y):
    hyp=(x**2+y**2)**0.5
    return hyp;

x=input("x:")
y=input("y:")
if  x>=0 and y>=0:
    hyp=hypo(x,y)
    print "Hypothenuse:", hyp
else:
    print "No negative, and zer0 numbers"
'''


#Exercise_2
from numpy import *
def minmaxvectors (mat1):
