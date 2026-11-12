names=input("Enter the names in a single row :").split()
dict={}
cnt=1
maxx=0
for i in names:
    if i in dict:
        cnt+=1
        dict[i]+=1
    elif i not in dict:
        dict[i]=1
        cnt=0
    if dict[i] > maxx:
        maxx=dict[i]
        name=i
print("THE WINNER IS :",name,maxx)    
