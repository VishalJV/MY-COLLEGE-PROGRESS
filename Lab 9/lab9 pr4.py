a=input().split()
max=0
min=int(a[0])
for jv in a:
    if int(jv)> max:
        max=int(jv)
    elif int(jv)<min:
        min=int(jv)
print(max)
print(min)