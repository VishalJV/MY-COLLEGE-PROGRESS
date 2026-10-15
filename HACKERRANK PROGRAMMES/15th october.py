n=int(input())
vishal=[]
for i in range(n):
    a=int(input())
    vishal.append(a)
maxi=vishal[0]
for v in range(len(vishal)):
    if vishal[v]>maxi:
        maxi=vishal[v]
        k=v ##### ee line missa ayyindi so silly mistake in this problem
print("Largest:",maxi)
print("Position:",k)
