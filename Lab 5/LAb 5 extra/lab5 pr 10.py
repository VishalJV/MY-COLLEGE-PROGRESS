a=int(input())
dig=0
for i in range(1,a+1):
    if a%i==0:
        print(i)
        dig+=1
print(dig)
if  dig==2:
    print("PRIME NUMBER")
else:
    print("NOT A PRIME NUMBER")