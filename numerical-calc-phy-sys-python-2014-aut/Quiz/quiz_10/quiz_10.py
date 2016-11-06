#Altug Yildirim
#Euler Prob. 1

sum=0
for i in range (1,1000):
    if i%3 == 0:
        sum=sum+i
    elif i%5 == 0:
        sum=sum+i

print 'Answer for the First Question is', sum

#Euler Prob. 2

def fib(number):
    if number==0:
        return 0
    elif number==1:
        return 1
    else:
        a=0
        c=1
        b=1
        for i in range(1,number):
            a,b=b,a+b
        return b

sum=0
i=0
while fib(i) <= 4e6:
    fib(i)
    if fib(i) >= 4000000:
        break
    elif fib(i)%2 == 0:
        sum=fib(i)+sum
    i=i+1
print 'Answer for the Second Question is', sum
