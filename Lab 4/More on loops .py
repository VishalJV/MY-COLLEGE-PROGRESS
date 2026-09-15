# #problem 1
# a=int(input())
# k=0
# print()
# while k<=a:
#     print(k, end=" ")
#     k=k+1
# #problem 2
# b=int(input())
# print()
# while b>=0:
#     print(b)
#     b=b-1
#problem 4
# for i in range (1,101): 
#     if i%2!=0:
#         print(f"{i}",end=" ")
#problem 6
# n=int(input())
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)
#problem 7
# k=int(input())
# sum=0
# for i in range(1,k+1):
#     if i%2==0:
#        sum=sum+i
# print(sum)
#problem 8
# k=int(input())
# sum=0
# for i in range(1,k+1):
#     if i%2!=0:
#        sum=sum+i
# print(sum)
#problem 9
# a=int(input())
# for i in range (1,11):
#     print(a,"X",i,"=",a*i,sep="")
#problem 10
# n=int(input())
# dig=0
# while n!=0:
#     n=n//10
#     dig+=1
# print(dig)
#problem 11
# a=int(input())
# v=a
# sum=0
# while a!=0:
#     sum=sum*10+a%10
#     a=a//10
# print(sum%10+v%10)
#problem 12
# a=int(input())
# v=a
# sum=0
# while a!=0:
#     sum=sum*10+a%10
#     a=a//10
# print(sum%10,v%10)
#problem 13
# a=int(input())
# rev=0
# while a!=0:
#     rev=rev*10+a%10
#     a=a//10
# print(rev)
#problem 14
# a=int(input())
# dig=0
# while a>0:
#     dig+=1
#     a=a//10
# print(dig)
#problem 15
# a=int(input())
# pro=1
# while a!=0:
#     pro=pro*(a%10)
#     a=a//10
# print(pro)
#problem 16
# a=int(input())
# v=a
# rev=0
# while a!=0:
#     rev=rev*10+a%10
#     a=a//10
# if v==rev:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")
#problem 17 WAP to find frequency of each digit in a given integer.
# a=int(input())
# d0=0
# d1=0
# d2=0
# d3=0
# d4=0
# d5=0
# d6=0
# d7=0
# d8=0
# d9=0
# while a!=0:
#     b=a%10
#     a=a//10
#     if b==0:
#         d0+=1
#     if b==1:
#         d1+=1
#     if b==2:
#         d2+=1
#     if b==3:
#         d3+=1
#     if b==4:
#         d4+=1
#     if b==5:
#         d5+=1
#     if b==6:
#         d6+=1
#     if b==7:
#         d7+=1
#     if b==8:
#         d8+=1
#     if b==9:
#         d9+=1
# print("No of 0's",d0)
# print("No of 1's",d1)
# print("No of 2's",d2)
# print("No of 3's",d3)
# print("No of 4's",d4)
# print("No of 5's",d5)
# print("No of 6's",d6)
# print("No of 7's",d7)
# print("No of 8's",d8)
# print("No of 9's",d9)

#problem 18 WAP to check whether a number is Armstrong number or not
# a=int(input())
# v=a
# m=a
# dig=0
# sum=0
# while a!=0:
#     dig=dig+1
#     a=a//10
# while v!=0:
#     b=v%10
#     v=v//10
#     sum=sum+b**dig
# print(sum)
# if sum==m:
#     print("Armstrong Number")
# else:
#     print("Not a Armstrong Number")
#problem 20 WAP to check whether a number is Perfect number or not
# firs time  we need to extract all the divisors  







##########################      STAR PROBLEMS ################









#star problems  square star pattern 
# a=int(input())
# for i in range(1,a+1):
#     for j in range(1,a+1):
#         print("*",end="")
#     print()
    
# star problem 2  Hollow Mirrored Right Triangle Star Pattern

# a=int(input())
# for i in range(1,a+1):
#     for j in range(1,a+1):
#         if j>=i:
#             print("*",end="")
#     print()

#problem 3 Hollow Mirrored Rhombus Star Pattern
# a=int(input())
# for i in range (1,a+1):
#     for j in range (1,i+1):
#         print("*",end="")
#     print()
#problem 4   Hollow Pyramid Star Pattern
# a=int(input())
# for i  in range(1,a+1):
#     for j in range(1,a+1):
#         if j>=i:
#             print("*",end=" ")
#         else:
#             print(" ",end="")
#     print()
# #problem 5   Inverted Mirrored Right Triangle Star Pattern
# a=int(input())
# for i  in range(1,a+1):
#     for j in range(a+1,0,-1):
#         if j<=i:
#             print("*",end=" ")
#         else:
#             print(" ",end="")
#     print()
# #problem 6 Square Star Pattern

# a=int(input())
# for i in range (1,a+1):
#     for j in range(1,a+1):
#         if i==1 or i==a:
#             print("*",end="")
#         elif j==1 or j==a:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# # #problem 7  Right Triangle Star Pattern
# a=int(input())
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         if j==a or j==i  or j==1  or i ==a:
#             print("*",end="")
#         else:
#             print(" ",end="") 
#     print()

# #problem 8 Hollow Inverted Pyramid Star Pattern
# a=int(input())
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# for k in range(a-1,0,-1):
#     print(k*"*",end="")
#     print()
        
#problem 9
