a=int(input())
if a!=0:
    pro=1
elif a==0:
    pro=0
while a>0:
    b=a%10
    a=a//10
    pro=pro*b
print(pro)

