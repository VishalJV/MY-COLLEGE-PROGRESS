a=int(input())
fac=1
while a>1:
    fac=fac*a
    a=a-1
print(fac)
if a==0 :
    print(1)
elif a<0:
    print("Invalid Input")
