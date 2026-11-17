# functions 
# Parameter = Placeholder   parameter pehle define honi chahiye
# Argument = Actual value  argument jab we call we need to use argument we need to argue with the function to make our work done
# two types untai builtin and user defined
def greet(name):
    print("hello",name)
    print("CODE EXECUTED !!!")
for i in range(10):
    greet(123)

## function defiine chesetappudu manam ecchey variables peeru parameters
# fnnction ni call chesinappudu manam icchey values arguments
def jogu_bro(name):
    print("KYA DEKH RHA H?",name)## parameters

jogu_bro("VISHAL")## argument

def student_info():
    name=input("Enter students name :")
    place=input("Enter students place :")
    print(name)
    print(place)

# student_info()
def addition(a,b):
    addd=a+b
    return addd
print(addition(2,999))


def calculate(a,b,oper="add"):
    if oper =="add":
        return a+b
    elif oper =="subtract":
        return a-b
    elif oper =="multiply": 
        return a*b
    else:
        return("INVALID OPERATION RA UNGAA")
print(calculate(3,2,"divide"))



def bill(a,b,disc=0):
    act=a*b
    fin=act-act*disc
    return fin

bill()
x=10
def vishal():
    global x 
    x+=5
    return x
c=vishal()
print(c)

si=input().split()
a=list(map(int,input().split()))
cnt=0
cnt1=a[0]
cnt2=0
sett=set()
for num in a:
    cnt+=1
    cnt2=cnt1
    cnt1=num
    if cnt >= int(si[1]) and cnt2==cnt1:
        sett.add(num)
        cnt=0
    #cnt=0
for i in sett:
    print(i,end=" ")
    print(len(sett))




vis=int(input())
a=list(map(int,input().split()))
lst=[]
cnt=0
for num in a :
    if num not in lst:
        lst.append(num)
    elif num in lst:
        lst.pop(num)
print(lst[1])




n=int(input())









