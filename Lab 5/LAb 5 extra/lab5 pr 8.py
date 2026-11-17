a=int(input())
for i in range(1,a+1):
    for j in range(i):
        if i>=j:
            print("*",end=" ")
    print()