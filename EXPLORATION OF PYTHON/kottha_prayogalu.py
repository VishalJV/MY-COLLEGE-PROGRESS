# # # # # # okay maaw ippudu def ane function gurinchi nerchukundamu 
# # # # # print("start")
# # # # # def vishal():
# # # # #     print("function work ayyindi maawa")
# # # # #     print("enjoy fandagowww")
# # # # # print("end ") ###############   ippiudu mana pythin always line by line veltundi kada so ee programme ni run chesinappudu manaki output emi vastundi check chei 
# # # # # # we will get out put as start and end no def work ayyindi maawa ee string print kaadu so see the working of the def function
# # # # # #ippudu inko condition raddamu for exapmle nen oka input teesukoni aa condition true aithey def function work ayyela chuddamu 
# # # # # vishal()

# # # # a,b=map(int,input().split())
# # # # n=a+b
# # # # k=a-b
# # # # x=n/2
# # # # print(n)
# # # # print(k)
# # # # print(f"{x:.2f}")
# # # # print("*")
# # # # for i in range(1,6):
# # # #     for j in range(i):
# # # #         print(" ",end="")
# # # #     for k in range(i):
# # # #         print("*",end="")
# # # #     print()
# # # # def vishal(name):
# # # #     print("HELLO",name.upper())

# # # # vishal("syam")

# # # # def dig():
# # # #     a=0
# # # #     dgt=0
# # # #     n=int(input())
# # # #     while n!=0:
# # # #         a=n%10
# # # #         n=n//10
# # # #         dgt+=1
# # # #     if n==0:
# # # #         dgt=1
# # # #     return (dgt)
# # # # x=dig()
# # # # print(x)

# # # # def greet(name):
# # # #     print("hello",name.lower())
# # # # greet("Vishal")

# # # '''
# # # 1.digit extracter
# # # 2.amstrong number
# # # 3.strong number
# # # 4.perfect number
# # # 5.print number
# # # 6.area of a pentagon
# # # 7. areas of common shapes'''

# # # # def digit():
# # # #     x = int(input())
# # # #     d = 0
# # # #     while x!= 0:
# # # #         s = x % 10
# # # #         d = d*10 + s
# # # #         x = x // 10
# # # #     a = d
# # # #     while a != 0:
# # # #         dgt = a % 10
# # # #         a = a // 10
# # # #         print(dgt)
# # # # digit()

# # # # def amstrong():
# # # #     x = int(input())
# # # #     a = x
# # # #     s = x
# # # #     count = 0
# # # #     sum = 0
# # # #     while x != 0:
# # # #         d = x % 10
# # # #         count += 1
# # # #         x = x// 10
# # # #     while a != 0:
# # # #         b = a % 10
# # # #         a = a // 10
# # # #         sum += b**count
# # # #     if sum == s:
# # # #         return ("Amstrong number")
# # # #     else:
# # # #         return ("Not an amstrong number")
# # # # j = amstrong()
# # # # print(j)

# # # def strong():
# # #     x = int(input())
# # #     a = x
# # #     fact = 1
# # #     sum=0
# # #     while x != 0:
# # #         d = x % 10
# # #         x = x // 10
# # #         while d>0:
# # #             fact=fact*d
# # #             d-=1
# # #         sum+=fact
# # #         print(fact)
# # #     # if sum == a:
# # #     #     print("Strong number")
# # #     # else:
# # #     #     print("Not a strong number")
# # # strong()
# # n=int(input())

# # sum=0
# # while n!=0:
# #     a=n%10
# #     n=n//10
# #     while a>0:
# #         fact=1
# #         fact=fact*a
# #         a=a-1
# #     sum=sum+fact
# # print(sum)
# for i in range(1,14):
#     print(" ",end= " ")
#     for j in range(i,1,-1):
#         print("*",end=" ")
#     print()
# python-3.11 is fast and reliable!

################  coding contest 9 one test case fail problem  #####################
# a=str(input())
# word=0
# longword=0
# lent=0
# vis="abcdefghijklmnopqrstuvwxyz"
# if len(a)<=1000:
#     for i in a:
#         if i in vis: 
#             lent+=1 #######maawa nuvvvu character  ni restrict chestunnav do not do that instead of that em use chestav antey if the character is space then word=word+1
#                     ###lekapothey if the char is not space then longword+=1 ekkadanee nee case fail ayyindi 
#                     # replace  if i in vis:  with if i !=" ": all of the code is perfect except the restriction case.........
#         if lent>longword:
#             longword=lent
#         if i==" ":
#             word+=1
#             lent=0
#         if a[0]==" " or a[-1]==" ":
#             word=word-1
#         if i not in vis:
#             longword+=1

            
#     print("Words:",word+1)
#     print("Longest Word Length:",longword)
# n=int(input("Enter the no of students :"))
# i=0 
# log=[]
# common = {0}
# not_common={0}
# cnt=0
# while i!=n:
#     a=input().split()
#     i+=1
#     log.append(a)               ## log.append anedi loop lopale ivvali or else a value always change aytundi kabbai append chesi tarvatha vaadukuntamu 
# for a in range(-1,len(log)-1):
#     i=log[a]
#     for b in range(len(log[a])):
#         j=i[b]
#         if j in log[a+1]:
#             common.add(j)
#         elif j not in log[a+1]:
#             not_common.add(j)
# common.remove(0)
# not_common.remove(0)
# fin_cmn_lst=[]
# fin_nt_cmn_lst=[]
# for jv in common:
#     fin_cmn_lst.append(jv)
# for jv2 in not_common:
#     fin_nt_cmn_lst.append(jv2)
# for m in fin_nt_cmn_lst:
#     if m not in fin_cmn_lst:
#         cnt+=1
# print(fin_cmn_lst)
# print(fin_nt_cmn_lst)
# print(cnt)
# #print(log)

# jv={1,3,4,2}
# jv.remove(1)
# print(jv)
# netflix=set(map(str,input().split()))
# prime=set(map(str,input().split()))
# hotstar=set(map(input().split))
# all_rounders=set()
# only_netflix=set()
# exclusive=set()
# a=netflix.intersection(prime,hotstar)
# b=netflix-a
# c=netflix.intersection(prime)
# d=prime.intersection(hotstar)
# e=hotstar.intersection(netflix)
# f=netflix&prime&hotstar
# jv=f-a-c-d-e
# all_rounders.add(a)
# only_netflix.add(b)
# exclusive.add(f)
# print(list(exclusive))
# print(list(all_rounders))
# print(list(only_netflix))
# master=set(map(input().split()))
# role_A=set(map(input().split()))
# role_B=set(map(input().split()))
# if role_A.issubset(master) and role_B.issubset(master):
#     print("VALID")
# else:
#     print("INVALID")
# if role_B.isdisjoint(role_A):
#     print("NO CONFLICT")
# else:
#     print("CONFLICT")
# b=set(role_B^role_A)|set(role_A^role_B)
# print(b)
# main=set(input().split())
# n=int(input("Enter the no of sets :"))
# i=0
# while i!=n:
#     sattt=set(input().split())
#     if sattt.issubset(main):
#         a=True
#     else:
#         a=False
#     if a==True:
#         b=1
#     else:
#         b=0
#     i+=1
# if b==1:
#     print("True")
# else:
#     print('False')
# n=int(input())
# i=0
# count=set()
# cnt=0
# while i!=n:
#     a=input()
#     count.add(a)
#     i+=1
# for  i in count:
#     cnt+=1
# print(cnt)
a=int(input())
lst1=set(map(int,input()))
b=int(input())
lst2=set(map(int,input()))
fin=set()
fin.add(set(lst1)^set(lst2))
m=list(fin)
m.sort()
for _ in m:
    print(_)











