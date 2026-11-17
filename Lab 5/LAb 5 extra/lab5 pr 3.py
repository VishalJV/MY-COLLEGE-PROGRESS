n=int(input())
a=int(input())
big_bills=0
small_bills=0
while a!=-999:
    a=int(input())
    if a>n:
        big_bills+=1
    elif a<n:
        small_bills+=1
print(big_bills+1)
print(small_bills)