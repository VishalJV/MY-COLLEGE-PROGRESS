a=input().split()
first=a[0]
for ch in a:
    if  len(ch)> len(first):
        final=ch
    elif len(ch)== len(first):
        final=first
print(final)