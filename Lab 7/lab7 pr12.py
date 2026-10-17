# # Take a sentence as input and remove all the duplicate characters from the string.
# a=str(input())
# #b='abcdefghijklmnopqrstuvwxyz'
# for i in range(len(a)):
#     c=a[i]
#     if c in a:
#         a=a.replace(c,"")
# print(a)
## JV ko ek logic devlop hua kudh se ki ek empty string lete h aur each letter add krte h if the next adding letter or the character is not in the new string then add krlenge  if in case the coming char is in there in the new string then skip krlenge
## update space bi ek character h if it does no need to repaet in the new string so space ke liye you donot need to write a new logic 

a=str(input())
new_string=""
for v in range(len(a)):
    b=a[v]
    if b not in new_string:
        new_string+=b
    elif b in new_string:
        continue
print(new_string)