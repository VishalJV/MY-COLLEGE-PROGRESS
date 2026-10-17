a=int(input())
Block_1=0
Block_2=0
Block_3=0
Block_4=0
Block_5=0
if 0<=a<=10:
    while a!=-1:
        a=int(input())
        if 1<=a<=2:
            Block_1+=1
        elif 3<=a<=4:
            Block_2+=1
        elif 5<=a<=6:
            Block_3+=1
        elif 7<=Block_4<=8:
            Block_4+=1
        elif 9<=a<=10:
            Block_5+=1
else:
    print("Enter a number in the given range")
print()
print()
print(Block_1)
print(Block_2)
print(Block_3)
print(Block_4)
print(Block_5)
#### not DONE 