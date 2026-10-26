a1=int(input("Enter the a1 coordinate :"))
b1=int(input("Enter the b1 coordinate :"))
a2=int(input("Enter the a2 coordinate :"))
b2=int(input("Enter the b2 coordinate :"))
c1=int(input("Enter the c1 coordinate :"))
c2=int(input("Enter the c2 coordinate :"))
if (a1/a2)!=(b1/b2):
    y = (a2*c1 - a1*c2)/(a2*b1 - a1*b2)
    x = (c1*b2 - c2*b1)/(a1*b2-a2*b1)
    print(f"The point of Intersection is : ({x:.2f} , {y:.2f})")
elif (a1/a2)==(b1/b2):
    print("The lines are parallel to each other no point of Intersection")