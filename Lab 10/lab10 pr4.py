a=str(input("ENter the string :"))
dicto={}
for char in a: 
    if char in dicto.keys():
        dicto[char]+=1
    else:
        dicto[char] = 1
print(dicto)
## done
