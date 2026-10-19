# Read a string and remove all repeated characters, keeping only the first occurrence of each.
a=str(input("Enter a string :"))
new=''
for i in range(len(a)):
    b=a[i]
    if b not in new : 
        new+=b
print(new)