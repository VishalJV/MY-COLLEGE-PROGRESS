b1=0
b2=0
b3=0
b4=0
b5=0                
cnt=0
while True:
    a=int(input())
    if 1<=a<=2:
        b1+=1
        cnt+=1
    elif 3<=a<=4:
        b2+=1
        cnt+=1
    elif 5<=a<=6:
        b3+=1
        cnt+=1
    elif 7<=a<=8:
        b4+=1
        cnt+=1
    elif 9<=a<=10:
        b5+=1
        cnt+=1
    if a==-1:
        break

print()
print()
F1=(b1/cnt)*100
F2=(b2/cnt)*100
F3=(b3/cnt)*100
F4=(b4/cnt)*100
F5=(b5/cnt)*100
vis="#"
print(f"1-2:  {(int(F1)//10)*vis} {F1:.2f} %")
print(f"3-4:  {(int(F2)//10)*vis} {F2:.2f} %")
print(f"5-6:  {(int(F3)//10)*vis} {F3:.2f} %")
print(f"7-8:  {(int(F4)//10)*vis} {F4:.2f} %")
print(f"9-10: {(int(F5)//10)*vis} {F5:.2f} %")

## finally done :)