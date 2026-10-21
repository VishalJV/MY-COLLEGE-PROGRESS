a=str(input())
cnt=0
rev=''
cnt2=0
for i in range(len(a)):
    b=a[i]
    if b ==" ":
        print(cnt,end=" ")
        cnt=0
    elif b.isalpha():
        cnt+=1
for j in range(len(a)-1,-1,-1):
    v=a[j]
    rev+=v
    cnt2+=1
    if v==" ":
        break
print(cnt2-1)
