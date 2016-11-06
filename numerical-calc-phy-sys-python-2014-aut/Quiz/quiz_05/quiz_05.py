from pylab import *

S=[0.99]
I=[0.01]
R=[0.00]
a=0.7
b=0.2
t=[0]
sumSIR=0
for i in range(0,49):
    S.append(S[i]-a*I[i]*S[i])
    I.append(I[i]+a*I[i]*S[i]-b*I[i])
    R.append(R[i]+b*I[i])
    t.append(i+1)
    sumSIR=R[i]+I[i]+S[i]
    if  sumSIR <= 1.1 and sumSIR >= 0.9:
        continue
    else:
        print "Check the initial conditions, please!"
        break
xlabel('Time(Day)')
ylabel('SIR Variables(Percentage)')
plot(t,R, label="Recovered")
plot(t,S, label="Susceptible")
plot(t,I, label="Infected")
title('Plot of Susceptible, Infected, Recovered versus Time')
legend()
show()
