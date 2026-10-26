a=int(input("Enter a 3 digit number :"))
if 100 <= a<= 999:
    v=a
    c=a%10
    a=a//10
    b=a%10
    a=a//10
    sum=a+b+c
    if v%sum==0:
        print("Harshad number ")
    else:
        print("Not a Harshad number")
else:
    print("Enter a 3 digit number only")