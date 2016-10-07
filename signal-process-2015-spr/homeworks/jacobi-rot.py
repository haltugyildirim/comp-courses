import random
import numpy as np
from math import *

x = input("Enter the dimension of a symmetric matrix: ")
A=np.random.random((x,x))
q=1
p=0
for p in range(x-1):
    for q in range(x-1):
        if p != q:
            P=np.identity(x-1)
            if p > q:
                P[q,q]=c
                P[p,p]=c
                P[p,q]=s
                P[q,p]=-s
            else:
                P[q,q]=c
                P[p,p]=c
                P[p,q]=-s
                P[q,p]=s
            t=(A[q,q]-A[p,p])/(2*A[p,q])
            c=cos(t)
            s=sin(t)
            P=array([c,s],[c,-s])
            P_dag=np.matrix.H(P)
            D=dot(P_dag,A)
            D=dot(D,P)
