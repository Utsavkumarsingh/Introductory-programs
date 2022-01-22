from numpy import*
import math as m
n=int(input('enter the number of terms to be generated: '))
arr=zeros(n,int)
for i in range(0,n):
    arr[i]=m.pow(2,i)-1
print("\n\nminus series\n",arr)
brr=zeros(n,int)
for i in range(0,n):
    brr[i]=m.pow(2,i)+1
print("\n\nplus series\n",brr)