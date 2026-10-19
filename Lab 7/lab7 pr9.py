# Sort the elements of the list in descending order without using any inbuilt function.
# im assuming all the elements in the list are integers 
a=list(map(int,input().split()))
for i in range(len(a)):                 ## using for going trough out the list 
    for j in range(len(a)-1):           ## using for swaping the elements
        if a[j]<a[j+1]:                 ## if the first element is less than the next element to it then 
            a[j],a[j+1]=a[j+1],a[j]     ## swap the order of the elements in the list
print(a)
############ done with <<<< BUBBLE SORT METHOD >>>>############
# we can also do this sorting with other method as well<---------------- HERE IS THE FISHHHH

## jv tought if there are mixed data types in the list so how can we arrange all the element in the list as ascending or alphabetical order 
## JV should work on that thing
## Still NOT DONE explore more methods like this(notime for this particular topic exploration)
  