#Write a function count_vowels(s) that returns the number of vowels in the string s. Read a
#string, call the function and print the result.
vis=input("Enter the string :").lower()
def vowel_counter():
    cnt=0
    for ch in vis:
        if ch in "aeiou":
            cnt+=1
    print("Vowels :",cnt)
vowel_counter()
## done