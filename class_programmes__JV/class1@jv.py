# # marks=[85,75,65,78,69]
# # sum=0
# # for i in range(len(marks)):
# #     sum+=marks[i]
# # print(sum/len(marks))
# # for i in range(4):
# #     name=str(input())
# #     dob=int(input())
# #     student=[name,dob]
# #     print(student[i])
## indexing th eelements in the lists are same as the indexing in strings starts from 0 untill its len -1 the same concept applies here too 
# #___________________________first topic_________________________ (concatenation concept in lists )
# # ippudu naa daggaraa oka list undi  daaniki nen oka element concatenate chestunna just like  i did in string 
# list1=[1,2,3,4,5]
# list1=[0]+list1
# print(list1)
# ## important thing to notice in this is manamm order ela istunnam anedi chaala important ikkada  
# # case1---
# list1=list1+[9,0]
# print(list1)   #----- ee output verey untadi 
# #case2---
# list1=[9,0]+list1
# print(list1)     #--- ee output verey untadi 
# # i thing order importance is clear for you now........
# #_______________________2nd topic____________________ (nested lists)
# sm_lst=[1,["a","b","c"],2,3,44,[1,3,5,7,9]]
# # as the name suggest the concept in this is nested lists 
# print(sm_lst[5])
# print(sm_lst[1][2])   #   <--------------- this shows us to access the nested list elements using series of []
## as we studied in strings -ve indexing is also a part of the lists 
## here we can use the -ve indexing as a better approach while working with lists that need any reverse operations or something like that
## lists are mutable ( matlab manam lists ni modify cheskovacchu unlike strings and tuples( actually tupules antey endo kuda naaku telvadu aina kuda nen aa example vaaduthuunnna so be carefull at this paricular point ))
# #______________________topic 3_________________________   (append or extend)
# lista=[1,2,3]
# lista.append(9) ## append can take upto 1 argument only not more than that......
# print(lista)
# lista.extend('4456')  # <------------- this is extend idi em chestadi antey multiple arguments ni oke saari add chestadi in the list by the order only string ne add chestindi not integers or floating values
# print(lista)
#________________________topic 4_________________-----( remove(), pop() and clear())
# remove em chestadi antey aa given item ni total list nundey remove chestundi 
# foe example 
lista=["v","i","s","h","a","l","v","c"]
lista.remove("v") ###############----------remove
print(lista)  #<----------- this remove anedi only first time aa item dorkinappudu maatrame danni rmove chestundi not from the whole list 
# simple ga cheppali antey manaki eppudaithey given item first time vastundo aa list nundi aa item matrame only one time matrame remove aytundi if there arre multiple items we cant delete allof them 
lista.pop(2)  ##<-------- ee command enduku use avuthadi antey if we wnat to remove a specific index element then we need to use pop function manaki ee indexing itemm remove kaavalo andulo pop function lo istey the list will be updated
print(lista)
lista.clear()#<----------- ee commmand clear aa list total ni clear chestundi all the data in the list is gone we use this to empty a list 
print(lista)#################--------------clear
lista.insert(0,"iam")
lista.insert(1,"jogu")
lista.insert(2,"vishal")
print(lista)
b=lista.copy()  #<------------ cpoy function em chestadi antey manaki unnna list ni as it is copy chestadi and we can store it in a single variable 
print(b)
'''
sum=0
lista=[1,2,3,sum] #  lists lo kudaa variables ni store cheskovacchu
print(lista)

'''
 















 