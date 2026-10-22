a=int(input())
dig=0
for n in range(1,a+1):
    while n!=0:
        dig+=1
        n=n//10
    print(dig)