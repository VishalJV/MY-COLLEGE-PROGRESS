a=0
b=1
n=int(input())
for i in range(n-2):
    a=a+b
    b=b+a
    print(a,b,end=" ")
if n==2:
    print(a,b)
