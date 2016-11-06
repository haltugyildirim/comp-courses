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
