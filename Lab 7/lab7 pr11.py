# Take a paragraph as input and find the count of digits, alphabets, and special characters present 
# in the paragraph. For alphabets, also check how many of them are upper case and how many are 
#lower case alphabets. Use inbuilt string functions to check.
a=str(input())
dig=0                                   ## declaring variables for each type of characters in the paragraph 
alp=0
spl=0
for i in range(len(a)):
    if a[i].isalpha():                  ## checking if the char is alphabet
        alp+=1
    elif a[i].isnumeric():              ## checking of the char is number
        dig+=1
    else:
        spl+=1

print("The no of digits :",dig)
print("The no of alphabets :",alp)
print("The no of splchars :",spl)
# each character ko lelo and check krke input ki variables mai daalna ki if that taken part is integer or alphabet or any other special character

