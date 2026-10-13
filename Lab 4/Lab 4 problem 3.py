#Lab 4 problem 3
#problem3  
shape=str(input("Enter the shape that you want to claculate the area of :"))
if shape=="square":
    a1=int(input("Enter the side length of the square :" ))
    print("The area of the square of the given Dimentions :",round(a1*a1,3),"units")
elif shape=="rectangle":
    a1=int(input("Enter the length of the rectangle :"))
    a2=int(input("Enter the breadth of the rectangle :"))
    print("The area of the rectangle with given Dimentions :",round(a1*a2,3),"units")
elif shape=="circle":
    a1=int(input("ENter the radius of the circle :"))
    print("The area of the circle is :",round(3.1415926*a1**2,3),"units" )
elif shape=="triangle":
    a1=int(input("Enter the base length :"))   
    a2=int(input("Enter the height corresponding to the base you entered :"))
    print("The area of the triangle with given dimentions :",round(0.5*a1*a2,3),"units")
else:
    print("Enter a valid shape")