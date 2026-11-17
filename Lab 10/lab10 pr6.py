n=int(input())
def get_grade():
    i=0
    marks={}
    gra=''
    fin_marks={}
    while i!=n:
        a=input().split()
        mar=int(a[1])
        marks[a[0]]=mar
        if mar>80:
            gra="A"
        elif 60<=mar<=79:
            gra="B"
        elif 40<=mar<=59:
            gra="C"
        else:
            gra="D"
        fin_marks[a[0]]=gra
        i+=1
    print(fin_marks)
get_grade()
## donne