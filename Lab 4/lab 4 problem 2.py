#problem 2
passw="s3cr3t!P@ssw0rd"  
a=str(input("Enter the password :"))
if a==passw:
    print("Correct password")
else:
    print("Wrong password")
    while a!=passw:
        a=str(input("Enter the password :"))
        if a!=passw:
            print("Wrong password")
        else:
            print("Correct Password")