x1,y1=map(int,input("Enter x1 , y1 center of the circle : ").split(","))
x2,y2=map(int,input("Enter x2 , y2  a point : ").split(","))
r=int(input("enter the radius of the circle : "))
dis=((x2-x1)**2+(y2-y1)**2)**0.5
if dis<r:
    print("Interior point")
elif dis==r:
    print("On the Boundary")
else:
    print("Exterior Point")