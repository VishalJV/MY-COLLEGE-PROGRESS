# Read a string and rewrite it so that the characters at even positions 
# (0, 2, 4, …) are in uppercase and those at odd positions are in lowercase. 
# Characters that are not letters stay unchanged but still occupy a position
a=str(input("Enter a string :"))
stt=''
for v in range(len(a)):
    b=a[v]
    if v%2==0:                      ##  checks even position 
        if b.isalpha():             ##  checks each char is alphabet or not 
            b=b.upper()             ## converts them into upper ones if all the above conditions are true
            stt=stt+b
        elif b.isnumeric():         ## If then char is a number then skips the iteration 
            continue
    elif v%2!=0:                    ## checks odd positions 
        b=b.lower()                 ## converts them into lower ones
        stt=stt+b
        if b.isnumeric():
            continue
    if b==' ':                      ## its a spl case we do not nee dto alter spaces given in the example so                  
        stt+=b                      ## ifthere are spaces then it adds it
print(stt)