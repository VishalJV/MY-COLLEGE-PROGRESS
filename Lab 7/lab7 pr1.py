## Write a program to reverse a string without using inbuilt function.
a=str(input())
rev=''
for i in range(len(a)-1,-1,-1):
    b=a[i]
    rev=rev+b
print(rev)
