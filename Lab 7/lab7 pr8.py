#Write programs for the following by taking list of integers of arbitrary length as user input. Do not use any inbuilt list functions other than len().
# i. Find the sum of the elements in the list. 
# ii Find the product of the elements in the list.
# iii. Find the smallest element in the list of integers


#first problem
l=list(map(int,input().split()))        ## this is also a common line you will see in the coming codes 
sum=0                                   ## the inputs are stored in the form of list the way you wanted form the beggining of python.......
for i in range(len(l)):
    sum=sum+l[i]                        ## each element gets adds up in the list 
print(sum)


#second problem
l=list(map(int,input().split()))        ## again the same line
prod=1
for i in range(len(l)):
    prod=prod*l[i]                      ## multiplying all the elements in the list 
print(prod)


# third problem 
l=list(map(int,input().split()))        ## phir se same line 
mini=l[0]                               ## the logic here is that comparing every element in the list with any element and adjusting the code 
for i in l:                             ## if the next number in the list is greater than the selected element then the minimum remains the same 
    if i<mini:                          ## if the next selected element is minimum than the first fixed element then the minimum changes 
        mini=i
print(mini)
## inn this problem you need to access the list elements and do some opreations thats it nothing much is need to do 
## important is taking the inputs in the form of list, remember JV thats the catch here.

