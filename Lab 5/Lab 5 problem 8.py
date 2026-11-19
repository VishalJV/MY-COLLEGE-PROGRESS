##Take a sentence as input and using while loop count the number of capital letters, small letters, 
#digits, and special characters in the sentence. Do not use any inbuilt function
a=input().split()
cap=0
sma=0
numm=0
spl=0
for ch in a:
    if ch.isupper():
        cap+=1
    elif ch.islower():
        sma+=1
    elif ch.isnumeric():
        numm+=1
    elif ch !=" ":
        spl+=1
print(cap)
print(sma)
print(numm)
print(spl)
## done