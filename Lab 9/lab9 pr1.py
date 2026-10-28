a=input().split()
even=[]
odd=[]
for num in a :
    if int(num)%2==0:
        even.append(num)
    elif int(num)%2!=0:
        odd.append(num)
for j in odd:
    print(j,end = " ")
print()
for i in even:
    print(i,end = " ")

