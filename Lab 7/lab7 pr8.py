#Write programs for the following by taking list of integers of arbitrary length as user input. Do not use any inbuilt list functions other than len().
# i. Find the sum of the elements in the list. 
# ii Find the product of the elements in the list.
# iii. Find the smallest element in the list of integers


#first problem
l=list(map(int,input().split()))
sum=0
for i in range(len(l)):
    sum=sum+l[i]
print(sum)


#second problem
l=list(map(int,input().split()))
prod=1
for i in range(len(l)):
    prod=prod*l[i]
print(prod)


# third problem 
l=list(map(int,input().split()))
mini=l[0]
for i in l:
    if i<mini:
        mini=i
print(mini)
## inn this problem you need to access the list elements and do some opreations thats it nothing much is need to do 


