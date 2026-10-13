a=int(input())
v=a
sum=0
while a!=0:
    b=a%10
    a=a//10
    sum=sum*10+b
if sum==v:
    print("Palindrome")
else:
    print("Not a Palindrome")