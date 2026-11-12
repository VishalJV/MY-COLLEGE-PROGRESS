total=input().split()
runs=0
wkts=0
bndrys=0
rPo=[]
cnt=0
sumi=0
fin=[]
for itm in total:
    if itm.isnumeric():
        runs=runs+int(itm)
        if int(itm)==4 or int(itm)==6:
            bndrys+=1
    if itm=="W":
        wkts+=1
    cnt+=1
for runsss in total:
    if runsss.isnumeric():
        sumi+=int(runsss)
        rPo.append(sumi)
        if cnt>5:
            cnt=0
            runsss=0
fin.append(rPo[5])
m=rPo.pop()
fin.append(m)
print("Total Runs :",runs)
print("Total Wickets :",wkts)
print("Total boundary's :",bndrys)
print(fin)
