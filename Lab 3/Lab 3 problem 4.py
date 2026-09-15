a=int(input())
if 1000<=a<=9999:
    b=a%10
    a=a//10
    c=a%10
    a=a//10
    d=a%10
    a=a//10
    print("SUm of last two digits = ",b+c)
    print("Sum of first two digits = ",a+d)
    if b+c==a+d:
        print("Sum of the first 2 digits is equal to the sum of last two digits")
else:
    print("Enter a 4 digit number")