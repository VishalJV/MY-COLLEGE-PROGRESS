     ## problem 10 
pou=float(input("Enter the no of pound's of apples :")) 
n=float(input("Enter the cash given by the customer "))  
rem=pou*2.5-n
if rem>0:
    print("You owe :",rem,"$")
elif rem<0:
    print("Required cash is more than given ")
elif rem==0:
    print("You owe nothing to the customer")