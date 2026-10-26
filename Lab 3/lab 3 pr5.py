a=int(input())
dig=0
if 10000<=a<=99999:
    a5=a%10
    a//=10 
    a4=a%10
    a//=10
    a3=a%10
    a//=10
    a2=a%10
    a//=10
if a5 >= a4 and a5 >=a3 and a5>=a2 and a5>=a:
    maxi=a5
    pos=1
elif a4>=a5 and a4>=a3 and a4>=a2 and a4>=a:
    maxi=a4 
    pos=2
elif a3>=a5 and a3>=a4 and a3>=a2 and a3>=a:
    maxi=a3
    pos=3
elif a2>=a5 and a2>=a3 and a2>=a4 and a2>=a:
    maxi = a2 
    pos=4
elif a>=a5 and a>=a4 and a>=a3 and a>=a4 and a>=a2:
    maxi=a
    pos=5
print(maxi)
print(pos)