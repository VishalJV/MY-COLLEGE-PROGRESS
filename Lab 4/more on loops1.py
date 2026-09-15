#problem 1 WAP to print all natural numbers from 1 to n. - using while loop
a=int(input())
k=0
print()
while k<=a:
    print(k, end=" ")
    k=k+1
#problem 2 WAP to print all natural numbers in reverse (from n to 1). - using while loop
b=int(input())
print()
while b>=0:
    print(b)
    b=b-1
#problem 4 WAP to print all even numbers between 1 to 100. - using while loop
for i in range (1,101): 
    if i%2==0:
        print(f"{i}",end=" ")
#problem 5 WAP to print all odd numbers between 1 to 100. - using while loop
for i in range (1,101): 
    if i%2!=0:
        print(f"{i}",end=" ")
#problem 6 WAP to find sum of all natural numbers between 1 to n
n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
#problem 7 WAP to find sum of all even numbers between 1 to n.
k=int(input())
sum=0
for i in range(1,k+1):
    if i%2==0:
       sum=sum+i
print(sum)
##problem 8WAP to find sum of all odd numbers between 1 to n.
k=int(input())
sum=0
for i in range(1,k+1):
    if i%2!=0:
       sum=sum+i
print(sum)
#problem 9  WAP to print multiplication table of any number.
a=int(input())
for i in range (1,11):
    print(a,"X",i,"=",a*i,sep="")
#problem 10    WAP to count number of digits in a number
n=int(input())
dig=0
while n!=0:
    n=n//10
    dig+=1
print(dig)
#problem 11   WAP to find sum of first and last digit of a number.
a=int(input())
v=a
sum=0
while a!=0:
    sum=sum*10+a%10
    a=a//10
print(sum%10+v%10)
#problem 12   WAP to find first and last digit of a number
a=int(input())
v=a
sum=0
while a!=0:
    sum=sum*10+a%10
    a=a//10
print(sum%10,v%10)
#problem 13  WAP to swap first and last digits of a number
a=int(input())
rev=0
while a!=0:
    rev=rev*10+a%10
    a=a//10
print(rev)
#problem 14   WAP to calculate sum of digits of a number
a=int(input())
dig=0
while a>0:
    dig+=1
    a=a//10
print(dig)
#problem 15  WAP to calculate product of digits of a number
a=int(input())
pro=1
while a!=0:
    pro=pro*(a%10)
    a=a//10
print(pro)