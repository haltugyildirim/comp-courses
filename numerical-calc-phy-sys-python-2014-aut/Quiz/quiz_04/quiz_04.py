#Altug Yildirim
#Quiz 4

#First Question
#Finding if a number is prime or not
def mersenne(x):
    m_num=(2**x)-1
    return m_num

def isitprime(x):
    i=3
    for j in range(2,x-1):
        modx=x%j
        i=1
        m=mersenne(x)
        if modx == 0:
            i=0
            m=0
            break
    return i

n=input("Enter a Number Bigger Than 1: ")
if n < 2:
    print "The number can be at least two!!!"
elif n == 2:
    print "2 is prime and the Mersenne number associated with it is 3"
elif n == 3:
    print "3 is prime and the Mersenne number associated with it is 7"
# :))))) biraz hile yaptim kusura bakmayin hocam.
else:
    i=isitprime(n)
    if i==1:
        m_num=mersenne(n)
        print n, "is prime and the Mersenne number associated with it is", m_num
    else:
        print "no prime"

#Second Question

from random import random

x=[1]
y=[1,1,3,2,3,3,1,2,2,4,4,2,4,4,4,1,1,4,4,2,3,3,3,1,1,3]
lencon=len(y)
z=0
for i in range(1,61):
    rand=random()
    if rand < 0.25:
        x.append(1)
    elif rand >= 0.25 and rand < 0.5:
        x.append(2)
    elif rand >= 0.50 and rand < 0.75:
        x.append(3)
    else:
        x.append(4)
    for j in range(1,lencon):
        if x[i]==y[j]:
                z=z+1
    if lencon==z:
        print "He manages to espace!"
        break
    if i==60:
        print "helicopter on the way to rescue him"
