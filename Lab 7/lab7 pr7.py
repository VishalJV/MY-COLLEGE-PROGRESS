#Write a program to check if a string is palindrome or not without using any inbuilt function except len()
a=str(input("Enter the string :")).lower()
rev=''
for i in range(len(a)-1,-1,-1):  ## 3rd time appearing this line
    rev=rev+a[i]
if rev==a:
    print("Palindrome")
else:
    print("Not a Palindrome")
## making it reverse and comparing it with rthe actual string if it matches the actual string or not.