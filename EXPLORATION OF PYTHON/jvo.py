# for i in range(3):
#     for j in range(3):
#         if i==j:
#             break
#         else:
#             print("inner cont, i= ",i)
#     print("outer commplete i= ",i)
for i in range(1,6):
    for j in range(1,i+1):
        if j==1 or i==j:
            print("D",end=" ")
        elif (i+j)%2==0:
            print("R",end=" ")
        else:
            print("Y",end=" ")
    print()