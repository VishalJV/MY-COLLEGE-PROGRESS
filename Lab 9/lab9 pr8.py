a=input()
num=[]
summ=0
for item in a :
    if item.isnumeric():
        num.append(item)
print(num)
for numbers in num:
    summ=summ+int(numbers)
print("The total sum is :",summ)