# # a=int(input())
# # tot=0
# # while a!=0:
# #     while tot<10:
# #         b=a%10
# #         a=a//10
# #         tot+=b
# # print(tot)
# a=int(input())
# while 1000<=a<=9999:
#     d=a%10
#     a=a//10
#     c=a%10
#     a=a//10
#     b=a%10
#     a=a//10
#     # a= 1st digit 
#     # b =2nd digit
#     # c =3rd dig
#     # d= 4th dig 
# tot1=max(a,b,c,d)
# tot2=min(a,b,c,d)
# print(tot2,tot1,end="")
# print(a)
a=int(input())
for i  in range (1,a+1):
    for j in range(1,i+1):
        print(j,end="")
    for m in range(j-1,0,-1):
        print(m,end="")
    print()