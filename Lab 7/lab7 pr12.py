# Take a sentence as input and remove all the duplicate characters from the string.
a=str(input())
#b='abcdefghijklmnopqrstuvwxyz'
for i in range(len(a)):
    c=a[i]
    if c in a:
        a=a.replace(c,"")
print(a)
