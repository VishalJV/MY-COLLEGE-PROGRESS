n = int(input())
i=0
coun_capi={}
while i!=n:
    country=input().split()
    coun_capi[country[0]]=country[1]
    i+=1
capital=input()
if capital in coun_capi:
    print(country[1])
else:
    print("NOT FOUND")
## done
