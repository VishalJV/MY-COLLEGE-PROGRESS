a=int(input())
b=int(input())
rev=0
while a!=0:
    b=a%10
    a=a//10
    rev=rev*10+b
if rev==b:
    print("SAME")
else:
    print("NOT SAME")