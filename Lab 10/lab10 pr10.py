numbers=list(map(int,input().split()))
summ=0
avg=0
for i in numbers:
    summ+=i
fin=summ/len(numbers)
l=max(numbers)
s=min(numbers)
tup=()
for j in range(1):
    tup = tup +(s,l,fin)
print(tup)
## done