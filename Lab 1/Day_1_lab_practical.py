print("hello world")
#problem1
print("Hello JKLU! iam learning python")
#problem2
name= input("Enter your name and branch ",)
print("hello",name , "welcome to jklu")
#problem3
leng=int(input("Enter the length value in meters :"))
bre =int(input("Enter the Breadth value in meters :"))
fin=leng*bre
print("the area is",fin,"m^2")
#problem4
fet1=int(input("enter a length value in feets",))
fet2=int(input("enter a breadth value in feets",))
feet=0.305
print("The area of the rectangle is",fet1*fet2*feet**2,"sqfeet")
#problem5
int1=int(input("x="))
int2=int(input("y="))
if int2 % int1==0:
    print("Y is divisible by X")
else :
 print("Invalid input")  
#problem6  
int3=int(input("Enter a value",))
if int3%2==0:
    print("The given number is even ")
else :
  print("The given number is odd")    
#problem7
rad=int(input("enter a value less than 100 : "))
if rad>100:
    print("please input a lesser value")
if 1<=rad<=100:
    print("the area of circle is",rad*rad*3.141560,"units")
#problem8
temp1=int(input("enter the temp value in celcius scale ")) 
far=(9/5)*temp1+32
print("the temp in fahrenheit is ", far)
print("the temp in kelvin scale is " ,temp1+273,"kelvin")
#problem9
sec=int(input("enter time in seconds  :"))
if 1<=sec<=86400 :
    print(sec/60,":min",",",sec/3600,"hour")
else:
   print("Enter a lesser value than that")
#problem 10
att=int(input("enter your attendence percentage   :"))
if att<=75 :
   print("You are not eligible ")
if 75<att<=100    :
   print("You are eligible")
else :
   print("Enter a valid attendence percrntage")   
   #problem10 extra 
atm=int(input("Enter a 4 Digit value  :"))
if 1000<=atm<=9999   :
   print("This is a valid pin for your ATM")
else :
   print("enter a valid pin for Atm")
   