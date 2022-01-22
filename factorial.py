from numpy import*
n=int(input('enter the number of terms to be generated: '))
arr=zeros(n,int)
arr[0]=1
for i in range(0,n-1):
    arr[i+1]=arr[i]*(i+1)
print(arr)