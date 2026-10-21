a=str(input())
cnt=0
for i in range(len(a)):
    if a[i]!=a[len(a)-i-1]:
        cnt+=0.5
print(f"Changes required : {cnt:.0f}")