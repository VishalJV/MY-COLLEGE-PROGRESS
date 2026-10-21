a=str(input("Enter the string :")).lower()
c=str(input("Enter the char you want to search :")).lower()
cnt=0
for i in range(len(a)):
    b=a[i]
    if b==c:
        cnt+=1
        print("POSITIONS :",i)
print("COUNT :",cnt)
