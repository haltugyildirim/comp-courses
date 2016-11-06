#Four Numeric Data Types
#float
#integer
#long integer
#complex numbers
'''
#arithmetic operations
a=10
b=20
print "a=", a
print "b=", b
print "a+b=", a+b
print "a-b=", a-b
print "a/b=", a/b
print "a*b=", a*b
print "a%b=", a%b
print "a**b=", a**b
print "a//b=", a//b #floor division-float kismini atiyor sadece integer kimini veriyor

#Vectors and Matrices

myvector=[1,2,3,4]
mymatrix=[[1,2,3],[4,5,6],[7,8,9]]
print myvector
print mymatrix

#I/O
x=input("Enter x")
z=raw_input("What is your name")

#assigning

counter = 100 #integer
mils = 1000.0 #float
name = "john" #string

#multiple assignment
a = b = c = 100
a,b,c =1,20.0, "john"

#deleting reference
#del var
#or
#del var_a

#I/O example1
name=raw_input("Please Enter Your Name")
print "Nice to meet you", name

#I/O example2

x=input("Please enter number 1: ")
y=input("Please enter number 2: ")
z=x+y
print "The sum of",x, "and",y, "is" ,z
'''
'''
#I/O Example3

import datetime

now=datetime.datetime.now()
currentyear=now.year
myname=raw_input("What is your name?")
mybirth=input("What is your year of birth?")
yearsold=currentyear-mybirth

print "Dear",myname,"your age is,",yearsold
'''

#strings
str='Hello World!'
print str
print str[0]
print str[2:]
print str[2:5]
print str * 2
print str + 'Test'

#lists 
#ayni string gibi aslinda ama farkli data type olabiliyor elemanlar

mylist=['anc',2.0, 768]
print mylist
print mylist[0]
print mylist[:2]

#tuple
#ayni list gibi ama update edilmiyor bir de () ile kapatiliyor
#read only lists

mytuple=(1,'abc',5.0,10,2,3,7.56,'patates')
print mytuple
print mytuple[3:]
print mytuple[0]
print mytuple[1]

#dictionary

dict = {}
dict['one']="This is one"
dict[2]="This is two"
tinydict={'name':'john','code':6345,'dept':'sales'}

print dict['one']
print dict[2]
print tinydict
print tinydict.keys() #prints only keys
print tinydict.values() #prints only values

