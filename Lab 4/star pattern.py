# #problem 1 
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end="")
#     print()
# #problem 2 
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n : # printing the coordinates 
#             print("*",end="")
#         else:   # giving space for the remaining part 
#             print(" ",end="")
# #problem 4
# a=int(input())
# for i in range(a,0,-1):
#     print(i*" ",end=" ")# initially printing spaces 
#     print(a*"*",end="")# then adding stars to the printed spaces 
#     print()# shifting to next line 
#problem 6 
# a=int(input())
# for i in range(1,a+1):
#     for j in range(0,i-1):
#         print(" ",end=" ")
#     print(a*"*",end=" ")
#     print()
# #problem 8 
# a=int(input())
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# #problem 9 
# a=int(input())
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         if i==a or j==1 or j==i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# #problem 10 
# a=int(input())
# for i in range(a-1,0,-1):
#     for j in range(1,a):
#         if j<i:
#             print(" ",end="")
#         else:
#             print("*",end="")
#     print()
a=int(input())
for i in range(1,a+1):
    for j in range(1,a+1):
        if  j==a or i==a:
            print("*",end="")
        else:
            print(" ",end="")
    print()
