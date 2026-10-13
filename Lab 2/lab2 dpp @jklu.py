#problem 1
v1=int(input("Enter a number : "))
if v1%5==0 :
    print("Hi")
else :
    print("Bye")    
#problem 2
l=int(input("Enter length1 :  "))
b=int(input("Enter length2 :  "))
h=int(input("Enter height  :  "))
area=((l+b)/2)*h
print("The Area of the Trapezium is :",area,"Units")
#problem 3 
#  body mass index antey weight /(height)**2
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
  #problem4
v5=input("Enter a Alphabet :")
if v5=='a' or v5=='e' or v5=='i' or v5=='o' or v5=='u'or v5=='A' or v5=='E' or v5=='I' or v5=='O' or v5=='U' :
    print("its a vowel")
else :
    print("its a consonent")
#problem 4 another solution   
a=str(input()).upper()
if a=="A" or a=="E" or a=="I" or a=="O"or a=="U":
    print("Vowel")
else:
    print("Consonent")
 
   #problem5
bac1=2.19*10**14
bac2=4.68*10**14
tot=(bac2-bac1)*100
print("The total bacterial growth is :",tot)
#problem 6
mon=int(input("Enter the no of months :"))
print("Years :" ,mon//12,"Months :",mon%12)
#problem7
colour=input("Enter the colour  :")
mode=input("Enter the mode  :")
if colour=='red' and mode=='steady':
    print("Rain ahead")
if colour=='red' and mode=='flashy':
    print("snow instead")   
if colour=='blue' and mode=='steady':
    print("clear view")  
if colour=='blue' and mode=='flashy':
    print("clouds due")    
# problem8
com1=int(input("Enter the company's costs :" )) 
com2=int(input("enter the company's profits :"))
if com1-com2>0 :
    print("company is in losses")
if com1==com2 :   
    print("Break even") 
if com1<com2 :
    print("company is in profits")   
    #problem9
out=int(input("Enter the no of orders :"))
if out<=25 :
    print("the total cost = ",out*25) 
elif out>25 :
    print("The total cost =",out*20)       






























