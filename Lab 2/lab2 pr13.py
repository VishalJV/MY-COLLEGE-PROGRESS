sal=int(input("Enter your salary  in rupees :"))
ta=0.05*sal
da=0.1*sal
hra=0.2*sal
gross = ta + da + hra + sal
if gross < 300000:
    tax=0
elif  300000 < gross <= 1000000:
    tax=0.1*gross
elif 1000000 < gross <= 2500000:
    tax=0.2*gross
elif gross > 2500000:
    tax=0.3*gross
print("The tax is",tax,"rupees")