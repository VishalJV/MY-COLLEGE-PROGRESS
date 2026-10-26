a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
if a > b and a > c:
    print(a,'is reater than remaining numbers')
elif b > a and b > c :
    print(b,"is greater than the remaining numbers")
elif a==b==c:
    print("all numebers are same")
else:
    print(c,'is greater than remianing numbers')
