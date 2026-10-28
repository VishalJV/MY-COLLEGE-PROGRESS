total=input().split()
runs=0
wkts=0
bndrys=0
rPo=[]
cnt=0
summm=0
for itm in total:
    if itm.isnumeric():
        if cnt>5:
            cnt=0
            rPo.append(runs)
            runs=0
        runs=runs+int(itm)
        if int(itm)==4 or int(itm)==6:
            bndrys+=1
    if itm=="W":
        wkts+=1
    cnt+=1
    rPo.append(runs)
for ruu in rPo:
    summm+=ruu
print("Total Runs :",summm)
print("Total Wickets :",wkts)
print("Total boundary's :",bndrys)
print(rPo)