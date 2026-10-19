#Write a Python program that accepts a hyphen-separated sequence of words as input and prints 
#the words in a hyphen-separated sequence after sorting them alphabetically. Do not use any 
#inbuilt sorting function. 
a=list(map(str,input().split("-")))
for i in range(len(a)-1):
    for j in range(i):
        if ord(a[i-1][j-1]) > ord(a[i][j]):
            a.extend(a[i-1][j-1])
print(a)
### not donne 