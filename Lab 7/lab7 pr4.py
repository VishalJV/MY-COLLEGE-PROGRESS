#  A program that takes a string as input and checks where the string is a pangram or not. Note : Pangrams are words or sentences containing every letter of the alphabet at least once. For example : "The quick brown fox jumps over the lazy dog"
a=str(input()).lower()
b='abcdefghijklmnopqrstuvwxyz'
cnt=0
for i in range(len(a)):
    c=a[i]
    if c in b:
        cnt+=1
        b=b.replace(a[i],"A")
    elif c==" ":
        continue
if cnt==26:
    print("Pangram")
else:
    print("Not a pangram")

### in this programme i replaced the stirng ith a non countable element of A
# iam first converting the whole string into lower case and doing the operations so that i can make th eprogramme eaisily manageble
# if once a letter in the b string is replaced then the next time the the letter wont appear in the b string so it cannot replace the letter so it doesnt count the next letter if it repeats multiple times in the main string
# this code took me 30 - 45 min of my time but it was the most satisfying code in my lab 7 coding hour time 
 
