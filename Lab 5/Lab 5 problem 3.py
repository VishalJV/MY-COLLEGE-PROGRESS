a=int(input())
cnt=0
while True:
    b=int(input())
    if b%a==0:
        cnt+=1
    if b==-999:
        break
print(cnt)