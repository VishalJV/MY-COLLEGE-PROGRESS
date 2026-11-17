x=int(input())
y=int(input())
n=int(input())
dig=0
for i in range (x,y):
    if i%n!=0:
        print(i,end=" ")
        dig+=1
print()
print(dig)