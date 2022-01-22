import math as m
from numpy import *
n=longdouble(input('enter the number: '))
a=m.floor(n/2)+1
j=0
for i in range(2,a):
    if n%i==0:
        print(i," is a factor")
        j=j+1
if(j==0):
    print('prime number')