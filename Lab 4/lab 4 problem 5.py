v=int(input("Enter the no of kilometers that you want to Travel :"))
dn=str(input("Enter the mode Day / Night :"))
if v>=100:
    print("The total cost is :",round(v*2.88,4),"INR",end="")
elif 20<=v<100:
    print("The total cost is :",round(v*4.32,4),"INR",end="",)  
elif 0<=v<20:
    if dn=="Day":
        print("The total cost is :",round(v*37.8+33.58,4),"INR",end="")
    else:
        print("The total cost is :",round(v*43.17+33.58,4),"INR",end="")
        