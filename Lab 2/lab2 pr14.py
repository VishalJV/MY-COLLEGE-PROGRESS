inc=int(input("Enter your salary :"))
if inc <20000:
    tax = 0.2*inc
elif 20000 < inc <= 50000:
    tax = 400 + 0.25*(inc-20000)
elif  inc > 50000:
    tax = 1150 + 0.35*(inc-50000)
print("Your tax will be :",tax)