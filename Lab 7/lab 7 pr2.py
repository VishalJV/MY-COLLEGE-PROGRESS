#  Write a program to find the length of the last word in a sentence. 
a=str(input())
cnt=0
for i in range(len(a)):
    b=a[i]
    if b!=" ":
        cnt+=1
    elif b==" ":
        cnt=0
print(cnt)
## we can do this problem inn another method that is reversing the string and counting the letters untll we get a space
a=str(input())
rev=''
cnt=0
for i in range(len(a)-1,-1,-1):
    b=a[i]
    rev=rev+b
for i in rev:
    if i!=' ':
        cnt+=1
    elif i==' ':
        break
print(cnt)
