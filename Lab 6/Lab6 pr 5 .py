n=int(input())
lar1=0
lar2=0
for i in range(n):
    a=int(input())
    if a>lar1 and a>lar2:
        lar2=lar1
        lar1=a
    elif a<lar1 and a>lar2:
        lar2=a
print(lar1,lar2)

