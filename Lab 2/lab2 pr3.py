#problem 3 
#  body mass index means weight /(height)**2
v2=float(input("Enter the user's weight in KG :"))
v3=float(input("Enter the user's height in cm :"))
BMI=(v2/(v3)**2)*10000
print("Your Exact BMI is :",BMI)
if 0<=BMI<18.5 :
    print("You are underweight")
if 18.5<=BMI<=25 :
    print("You are normal weight")    
if 25<BMI<= 30 :
    print("YOu are over  slightly overweight")
if 30<=BMI<35 :
    print("You are obese")   
if BMI>=35 :
    print("You are clinically obese") 