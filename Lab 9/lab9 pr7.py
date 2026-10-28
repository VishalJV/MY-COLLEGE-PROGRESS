a=input().split()
word=''
rev=[]
for item in a:
    word=item[::-1]
    rev.append(word)
    word=''
for jv in rev:
    print(jv,end=" ")
