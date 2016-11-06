#Basic Constructions in Python
#if statement

'''
a=input("Enter a number")

if a<5:
    print "The number is less than 5"

print "thank you for using python"
'''
'''
var=100
if(var==100):print "Value is 100"
print "Bye"
'''

'''
a=input("Enter a number")
if a<5:
    print "number is smaller than 5"

elif a==5:
    print "number is 5"
else:
    print "the number is bigger than 5"

print "bye"
'''

'''
num1=input("Enter number 1")
num2=input("Enter number 2")


if num1<num2 and num1<0:
    print "Number 1 is smaller than number 2 and negative"

print "bye"
'''

'''
a,b=2,3
if not(a==b):
    print "they are not equal"
'''
'''
#range command
print range(1,10)
print range(1,10,3)

for i in range(1,10):
    print i

for i in range(1,10,2):
    print i
'''

'''
languages=['C++',"Lojban",'Fortran']

for index in range(len(languages)):
    print 'I learned', languages[index]

for i in range(1,10):
    for j in range(1,10):
        print i,"times",j,"is equals to",i*j
'''

'''
#while statement
#while=for+if

count=1
while(count<11):
    print 'The count is:', count
    count=count+1
print "Bye"
'''
'''
#continue command
for number in range(0,10):
    if number==5:
        continue
    print 'Current number:',number
'''

'''
#break command
for number in range(0,10):
    if number ==5:
        break
    print 'Current number:', number
'''

'''
#example1
for num in range(10,20):
    for i in range (2,num):
        if num%i==0:
            j=num/i
            print '%d equals %d * %d' %(num,i,j)
'''
'''
#example2
var=input("please put a number")
if var < 200:
    print "expression is less than 200"
    if var == 150:
        print "which is 150"
    elif var==100:
        print "which is 100"
    elif var==50:
        print "which is 50"
elif var < 50:
    print "Expression is less than 50"
else:
    print "Could not find the number"
'''

'''
#example n!
n=input("Input a number to calculate its' factorial: ")
j=1
for i in range(1,n+1):
    j=j*i
    print j
'''

#Fibonacci
number=input("Enter a Fibonacci Number to Calculate:")

if number==0:
    fibo=0
elif number==1:
    fibo=1
else:
    a=0
    c=1
    b=1
    for i in range(1,number):
        a,b=b,a+b
    fibo=b
print "The",number,"th Fibonacci Number is:",fibo
