n=int(input())
for i in range(1,n+1):
    for j in range(n-1,0,-1):
        print((j)*" ",end=" ")
    for k in range(1,i+1):
        print(i,end=" ")
    print()