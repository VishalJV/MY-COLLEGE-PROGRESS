## Write a program to reverse a string without using inbuilt function.
a=str(input())
rev=''                          ## new string mai add krte jaayenge bas
for i in range(len(a)-1,-1,-1): ## this line is seen more than 2 times in this lab 
    b=a[i]                      ## use that for loop logic where ever you get erversing logic
    rev=rev+b
print(rev)
