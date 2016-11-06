%defining Dt
dt=0.0012;

%defining the Dx
dx=1/20;

%creating the mesh grid for 1D and defining the boundary conditions for x
x_num=0:dx:1;

%defining mu
mu=dt/(dx)^2;

%coefficients
a=-mu;
b=1+2*mu;
c=-mu;
e=zeros(1,length(x_num-1));
f=zeros(1,length(x_num-1));
u=zeros(1,length(x_num-1));

%boundary conditions
for k=1:length(x_num)
  if (x_num(k)<0.5)
    u(k)=2*x_num(k);
  else (x_num(k)>=0.5);
    u(k)=2-2*x_num(k);
  end
end

%initial conditions
u(1)=0;
u(length(x_num))=0;

%coefficient d
d = u(2:length(x_num)-1);

for t=1:50
    d = u(2:length(x_num)-1);
    for k=2:length(x_num)-2
        e(k) = c/(b-a*e(k-1));
        f(k) = (d(k) + a*f(k-1))/(b - a*e(k-1));
    end

    for l=length(x_num)-3:-1:1
        d(l) = e(l)*d(l+1) + f(l);
    end
    u(2:length(x_num)-1)=d;
end

plot(x_num,u)

%This code didn@t work out but I could not understand why
%The plot below shows the output, but it is nonsense;