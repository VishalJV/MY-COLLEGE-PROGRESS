int_items=int(input())
i=0
int_dict={}
fin_dict={}
while i!=int_items:
    items=input().split()
    int_dict[items[0]]=int(items[1])
    i+=1
sold_items=int(input())
j=0
while j!=sold_items:
    items2=input().split()
    if items2[0]=="SELL":
        fin_dict[items2[1]]=int_dict[items[1]]-int(items2[2])
    elif items2[0]=='ADD':
        print()
    j+=1
print(fin_dict)
## not done