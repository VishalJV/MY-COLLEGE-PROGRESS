n=int(input())
i=0
email=[]
while i!=n:
    a=input().split()
    c=a[0].lower()+"."+a[1].lower()
    if c+"@jklu.edu.in" in email:
        c=c+str(i)
    b=c+"@jklu.edu.in"
    email.append(b)
    i=i+1
print()
print()
for emails in email:
    print(emails)
