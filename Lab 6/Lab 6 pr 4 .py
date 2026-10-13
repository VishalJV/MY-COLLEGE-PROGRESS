n=int(input())
rem=n%2
dig=0
while n!=0:
    n=n//2
    rem=n%2
    dig=dig*10+rem
print(dig[::-1])