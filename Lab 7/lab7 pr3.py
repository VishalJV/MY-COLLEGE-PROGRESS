sent=str(input("Entre the sentence :"))
find=str(input("Enter the word you need to find :"))
word=''
fin_word=''
cnt=0
sent=sent + ' '
for ch in sent:
    if ch ==' ':
        fin_word=word
        word=''
        if fin_word==(find) :
            cnt+=1
            fin_word=''
        continue
    word = word + ch
print(cnt)