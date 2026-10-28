a=input("Enter the string :")
word=''
lst=[]
a=a+" "
for ch in a:
    if ch!=' ':
        word=word+ch
    elif ch==" ":
        if len(word)>3:
            lst.append(word)
        word=""
print(lst)
## the other way 
a=input().split()
name=[]
for ch in a:
    if len(ch)>3:
        name.append(ch)
print(name)