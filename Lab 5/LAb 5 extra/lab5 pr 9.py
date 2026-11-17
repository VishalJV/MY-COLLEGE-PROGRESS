a=int(input("Enter a positive number : "))
dig=int(input("ENter a digit less than 10 : "))
cnt=0
while a!=0:
    b=a%10
    a=a//10
    if b==dig:
        cnt+=1
print("The no of times the digit appeared is :",cnt)