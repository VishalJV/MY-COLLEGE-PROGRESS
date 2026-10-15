#Write a program to check if a string is palindrome or not without using any inbuilt function except len()
a=str(input("Enter the string :")).lower()
rev=''
for i in range(len(a)-1,-1,-1):
    rev=rev+a[i]
if rev==a:
    print("Palindrome")
else:
    print("Not a Palindrome")