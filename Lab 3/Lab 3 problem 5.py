# a=int(input())
# dig=0
# if 10000<=a<=99999:
#     a5=a%10
#     a//=10 
#     a4=a%10
#     a//=10
#     a3=a%10
#     a//=10
#     a2=a%10
#     a//=10
# print(max(a,a2,a3,a4,a5))

for i in range(1,5):
    for j in range(i,0,-1):
        for k in range(i-1,-1):
