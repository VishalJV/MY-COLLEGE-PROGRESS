a=list(map(int,input("Enter the list :").split()))      ## the basic input variable so that every number can ber in form of list in the a variable
even=()                                                 ## created a new tuple for even numbers 
for num in a:
    if num%2==0:
        even=even+(num,)                                ## if the number selected in the a list is even then its added to the new even tuple
print(even)                                             ## printing the final tuple
##done