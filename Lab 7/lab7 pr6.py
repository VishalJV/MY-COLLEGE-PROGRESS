b1=0
b2=0
b3=0
b4=0
b5=0                
cnt=-1
while True:
    a=int(input())
    if 1<=a<=2:
        b1+=1
    elif 3<=a<=4:
        b2+=1
    elif 5<=a<=6:
        b3+=1
    elif 7<=a<=8:
        b4+=1
    elif 9<=a<=10:
        b5+=1
    if a<0 or a>0:
        cnt+=11
    if a==-1:
        break

print()
print()
print(f"1-2:   {((b1/cnt)*100):.2f} %")
print(f"3-4:   {((b2/cnt)*100):.2f} %")
print(f"5-6:   {((b3/cnt)*100):.2f} %")
print(f"7-8:   {((b4/cnt)*100):.2f} %")
print(f"9-10:  {((b5/cnt)*100):.2f} %")
#### not DONE 
## logic ??
# print(f"{(4/5):.3f}")
