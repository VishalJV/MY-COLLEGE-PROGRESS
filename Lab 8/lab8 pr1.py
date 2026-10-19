#Read a string and count how many characters in it are vowels, consonants, digits, spaces and other symbols
a=str(input("Enter a string :"))
vow=0
con=0
dig=0
spa=0
spl=0
for v in range(len(a)):
    b=a[v]
    if b==' ':
        spa+=1
    elif b in "aeiou":
        vow+=1
    elif b in "bcdfghjklmnpqrstvwxyz":   ## here we need to use not in bcoz if we dont the
        con+=1                           ## special chars will count in the consonoent variable which we don't need
    elif b  in "!@#$%^&*()_+-=}{][:""'<>,./?/~`" : ## all types of braces shoul always input in reverse so that the editor does not confuse.
        spl+=1
    elif b.isnumeric():                  ## isnumeric is a function check if b is an integer or not 
        dig+=1                           ## return type is bool i think...... (yup its returning boolean~)
print("No.of vowels =",vow)
print("No.of consonents =",con)
print("no.of special characters =",spl)
print("no of spaces =",spa)
print("No.of digits =",dig)

       