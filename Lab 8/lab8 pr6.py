a=str(input(""))
if a[0]=="R" and a[1]=="J" and a[4].isalpha() and a[5].isalpha() and a[2].isnumeric() and a[3].isnumeric() and a[6].isnumeric() and a[7].isnumeric() and a[8].isnumeric() and a[9].isnumeric():
    print("TRUE")
else:
    print("FALSE")
## thats a way to solve that question 
## the second way to solve this question is that :-
a=str(input())
for i in range(2):
    first_1=False
    b=a[i]
    if b=="R" or b=="J":
        first_1=True
for j in range(2,4):
    c=a[j]
    second_1=False
    if c.isnumeric():
        second_1=True
for k in range(4,6):
    d=a[k]
    third_1=False
    if d.isalpha():
        third_1=True
for l in range(6,10):
    e=a[l]
    fourth_1=False
    if e.isnumeric():
        fourth_1=True
if first_1==True and second_1==True and third_1==True and fourth_1==True:
    print("True")
else:
    print("False")