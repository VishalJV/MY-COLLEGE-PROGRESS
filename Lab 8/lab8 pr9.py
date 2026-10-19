#  At the college hackathon, teams receive their problem statement as a coded message. 
# To encode it, each letter of the original message is shifted forward by K positions in the alphabet 
# (with K = 3, a becomes d and c becomes f). If the shift goes beyond z, counting continues again from 
# a (with K = 3, y becomes b). Spaces are left as they are. Write the program that encodes a message so the organisers can prepare the clues.
#  Input: The first line contains the message, made up of lowercase letters and spaces only.
#  The second line contains the integer K.
a=str(input("Enter the string :"))
c=int(input("Enter the shift :"))
new=''     ## as we cant modify strings we need to take each and every element and add it to a new one
for i in range(len(a)):
    b=a[i]
    if b==" ":
        new+=b
    elif b!=' ':
        jv=c+ord(b) 
        if jv>122:
            jv= (jv-26)
        d=chr(jv)       ##  <------- this line took me 6 to 7 days to think and execute
        new+=d                ## basically that means d is another variable 
print(new)
