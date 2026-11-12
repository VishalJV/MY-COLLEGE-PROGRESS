# Read a list of integers and a value V. Convert the list into a tuple and print the tuple, its length,
#the number of times V occurs in it, and the index of the first occurrence of V
a=list(map(int,input("Enter the list :").split()))          ## used for mapping a list to a particular var in int format
vis=int(input())
cnt=0
fir=0               # first index var
tupp=tuple(a)       ## converting into tuple
for i in range(len(a)):
    m=a[i]
    if vis == m:
        cnt+=1
for j in range(len(a)):
    k=a[j]
    if k == vis:
        fir=j
        break
print("TUPLE :",tupp)
print("LENGTH :",len(tupp))
print("The Count of ",vis,"is",cnt)
print("FIRST INDEX :",fir)
## done


