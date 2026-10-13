n=int(input())
for i in range(1,n+2):
    for j in range(n,0,-1):
        if j>=i:
            print(" ",end="")
        elif j<i:
            print(j,end="")
        # print("*",end="")
    print()