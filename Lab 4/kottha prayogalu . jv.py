a=int(input())
b=int(input())
dig=0
for i in range (a,b+1):
    x=i%10
    j=i//10
    y=j%10
    while x>y:
        print(i)
        #problem 16 in more on loops maki it working in your free time
a=int(input())
dig=0
dig0=0
dig1=0
dig2=0
dig3=0
dig4=0
dig5=0
dig6=0
dig7=0
dig8=0
dig9=0
while a!=0:
    dig ==a%10
    a=a//10
    if dig ==0:
        dig0+=1
    elif dig ==1:
            dig1+=1
    elif dig ==2:
            dig2+=1
    elif dig ==3:
            dig3+=1
    elif dig ==4:
            dig4+=1
    elif dig ==5:
            dig5+=1
    elif dig ==6:
            dig6+=1
    elif dig ==7:
            dig7+=1
    elif dig ==8:
            dig8+=1
    elif dig ==9:
            dig9+=1
print (dig0,dig1,dig2,dig3,dig4,dig5,dig6,dig7,dig8,dig9)