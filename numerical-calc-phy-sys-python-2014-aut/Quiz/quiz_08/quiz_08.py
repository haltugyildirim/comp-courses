from numpy import *

def zero(M):
    check=0
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i,j]<=10**(-6):
                check+=1
    if check==(len(M)*len(M)):
        return 1
    else:
        return 0;

def matrixmultiply(M,p):
    for i in range(p):
        M=dot(M,M)
    return M;

def nilpotent(M,n):
    result=0
    for p in range(2,n+1):
        M_temp = matrixmultiply(M,p)
        if zero(M_temp)==0:
            result=-1
        else:
            result = p
            break
    return result;

M = zeros((3,3))
print "Write the elements of an 3x3 matrix: "
for i in range (len(M)):
    for j in range (len(M)):
        M[i,j]=input()
print M

n=input("Enter the number of tries: ")

nil = nilpotent(M,n)

if nil == -1:
    print "No nilpotent."
else:
    print "The matrix M is nilpotent at", nil
