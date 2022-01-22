from numpy import*
a=int(input('           Enter the first number of fabonachi sequence: '))
b=int(input('           Enter the second number of fabonachi sequence: '))
l=int(input('           enter the number of terms to be generated: '))
print('\n\n\n')
arr=zeros(l,longdouble)
arr[0]=longdouble(a)
arr[1]=longdouble(b)
for i in range(2,l):
    arr[i]=arr[i-1]+arr[i-2]
print('         The fabonachi sequence generated from given starting numbers is:')
for j in range(0,l):
    print('         ',arr[j],end=' ')