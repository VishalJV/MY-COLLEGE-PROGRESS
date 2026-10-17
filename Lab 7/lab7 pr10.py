#Write a Python program that accepts a hyphen-separated sequence of words as input and prints 
#the words in a hyphen-separated sequence after sorting them alphabetically. Do not use any 
#inbuilt sorting function. 
a=str(input().lower()).split("-")   ## why is it returning me a list???
for i in range(len(a)):
    for j in range(len(a)-1):
        if ord(a[i][j]) > ord(a[i+1][j]):
            b=a.pop(i+1)
            a.insert(i,a[i+1][j])
print(a)