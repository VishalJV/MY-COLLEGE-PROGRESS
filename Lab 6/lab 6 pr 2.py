n=int(input())
i=1
while i<=1000:
    if i%n!=0 or i%4==0:
        i+=1
        continue 
    elif i%n==0:
        print(i,end="  ")
    i+=1