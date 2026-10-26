a=str(input())
cnt1=0
cnt2=0
for i in range(0,len(a)+0):
    a1=a[i-1]
    a2=a[i]
    if a1==a2:
        cnt1+=1
        v=a[i]
    elif a1!=a2:
        cnt2=cnt1
        cnt1=0
        continue
if cnt1<cnt2:
    print(v)
if cnt1==cnt2:
    print()

