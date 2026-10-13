a=int(input())
fac=1
if a<0:
    print("Invalid Input")
else:
    while a>1:
        fac=fac*a
        a=a-1
    print(fac)

