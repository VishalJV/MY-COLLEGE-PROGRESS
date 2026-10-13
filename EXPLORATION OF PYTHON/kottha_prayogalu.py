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
a=str(input())
word=0
longword=0
lent=0
vis="abcdefghijklmnopqrstuvwxyz"
if len(a)<=1000:
    for i in a:
        if i in vis: 
            lent+=1 #######maawa nuvvvu character  ni restrict chestunnav do not do that instead of that em use chestav antey if the character is space then word=word+1
                    ###lekapothey if the char is not space then longword+=1 ekkadanee nee case fail ayyindi 
                    # replace  if i in vis:  with if i !=" ": all of the code is perfect except the restriction case.........
        if lent>longword:
            longword=lent
        if i==" ":
            word+=1
            lent=0
        if a[0]==" " or a[-1]==" ":
            word=word-1
        if i not in vis:
            longword+=1

            
    print("Words:",word+1)
    print("Longest Word Length:",longword)
