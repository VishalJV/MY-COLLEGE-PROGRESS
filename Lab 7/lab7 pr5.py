# The Caesar cipher is a simple encryption technique that was used by Julius Caesar to send secret messages to his allies. It works by shifting the letters in the plaintext message by a certain number of positions, known as the “shift” or “key”. Take a string as input from user which contains English alphabets only in lower or upper case. Also, take the shift (an integer) as input from the user. Write a program to convert the string into its corresponding Ceaser Cipher which also contains English alphabets only. 
a=str(input("Enter a string :")).lower()
shift=int(input("No of characters you want to shift :"))
new=''
shift = shift % 26
for v in range(len(a)):
    b=a[v]
    jv=shift+ord(b)
    if jv>122:
        jv-=26
    d=chr(jv)
    new+=d
print(new)

