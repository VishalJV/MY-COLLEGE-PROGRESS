a=input().split()
for i in range(len(a)) :
    item=a[i]
    if item.isnumeric():
        if int(item)==0:
            b=a.pop(i)
            a.append(b)
print(a)

