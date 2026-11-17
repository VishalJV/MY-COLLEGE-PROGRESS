sent=str(input("Entre the sentence :"))                 ## ye to sentence kaa input le liya maine
find=str(input("Enter the word you need to find :"))    ## ye kis word ko find krna vo h input
word=''                                                 ## ye 1st main variable h 
fin_word=''                                             ## ye second main variable h
cnt=0                                                   ## using a count variable
sent=sent + ' '                                         ## i added a extra space for the whole sentence (iska use last mai pta chalyaega)
for ch in sent:
    if ch ==' ':                                        ## if there is space then the word variables update hota jaayega every time
        fin_word=word
        word=''
        if fin_word==(find) :                           ## agar vo word variables humara initial letter se match hota h to cnt +1 add hojayega
            cnt+=1
            fin_word=''
        continue
    word = word + ch                                    ## remaining code is for clearing the data for the next loop
print(cnt)                                              ## printing the count of the letter we gave as input