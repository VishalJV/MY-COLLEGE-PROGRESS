# Take a sentence and a word as input and check if the string contains the word in it. Also, count the number of times that word occurs in the string. Do this by using inbuilt string functions and then without using inbuilt string functions
a=str(input("Enter the string :"))
b=str(input("Enter the word :"))
word=''
cnt=0
for i in range(len(a)):
    b=a[i]
    if b in a:
        cnt+=1
    elif b==' ':
        continue

print(cnt)
## not DONE



