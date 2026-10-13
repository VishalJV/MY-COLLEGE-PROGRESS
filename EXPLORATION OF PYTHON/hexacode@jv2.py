# input any hexa value and convert it into 0 and 1 with using python
num1=input("Enter a hexa value",)
if len(num1) == 1:
    print("Single digit  hex value")
if len(num1) == 2:
    print("Double digit hex value")
if len(num1) == 3:
    print("triple digit hex value")
if len(num1) == 4:
    print("Quard digit hex value")            
else:
    print("Enter digits less than 4")