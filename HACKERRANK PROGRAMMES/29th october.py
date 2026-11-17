n=int(input())
books=set(map(int,input().split()))
cnt=1
for j in books:
    if j+1 in books:
        cnt+=1    
    else:     
        break
print(cnt)

