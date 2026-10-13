# ##pop concept 
# #pop em chestadi antey remove the last one on the like pulling a book from a stack of books
marks=[1,2,3,4,5,6,7,8]
# marks.insert(2,"vishal")

# print(marks)
max=0
min=marks[0]
for i in range(len(marks)):
    if marks[i]>max:
        max=marks[i]
    if marks[i]<min:
        min=marks[i]
print(max)
print(min)


