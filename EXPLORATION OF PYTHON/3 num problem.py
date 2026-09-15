num1=int(input("enter a value ",))
num2=int(input("enter a value ",))
num3=int(input("enter a value ",))
if num1-num2>0 and num2-num3>0 :
    print(num1)
if num2>num3 :
    print(num2)    
else:
    print(num3)    
if num1>num2>num3  :
    print(num1,num2,num3)   
if num2>num1>num3  :
    print(num2,num1,num3)  
if num2>num3>num1  :
   print(num2,num3,num1)  
if num3>num2>num1 :
    print(num3,num2,num1)
if num3>num1>num2:
    print(num3,num2,num1)
if num1>num3>num2 :
    print(num1,num3,num2)
if num1+num2>num3 :
    print("This can be a triangle")
else :
    print("This cant be a triangle")    
    