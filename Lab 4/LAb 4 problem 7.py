bud=int(input("Enter the budget for Trip :"))
sea=str(input("Enter the season that you want to go Trip in :"))
if 0<=bud<=100:
    if sea=="Summer":
        print("You aree going somewhere in Bulgaria with :",bud*0.3,"BGN")
    elif sea=="Winter":
        print("You are going somewhere in Bulgaria with :",bud*0.7,"BGN") 
    else:
        print("Enter a valid season")  
elif 101<=bud<=1000:
    if sea=="Summer":
        print("You are going to Balkans with :",bud*0.4,"BGN")  
    elif sea=="Winter":
        print("You are going to Balkans with :",bud*0.8,"BGN")
    else:
        print("Enter a valid season")
elif bud>1000:
    print("You are going to Europe with ")    











