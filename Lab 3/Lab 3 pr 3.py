a1=int(input())
a2=int(input())
a3=int(input())
if a1==0 or a2==0 or a3==0 :
    print("Invalid input")
elif a1+a2+a3==180:
    print("This can form a triangle")
    if a1>90 or a2>90 or a3>90:
        print("Obtuse angled triangle ")
    elif a1==90 or a2==90 or a3==90:
        print("Right angled triangle ")
    else:
        print("Acute angled triangle ")
else:
    print("This cannot form a triangle")

