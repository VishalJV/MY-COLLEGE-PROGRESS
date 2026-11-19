n=int(input())
rev_str=0                           ## ek partial use ke liye variable le liya maine 
while n !=0:                        ## mujhe division repeat honi chahiye until the remainder is less than 7
    remainder=n%8                   ## this is a variable for remainder
    n=n//8                          ## n value update hota jaa rha h
    rev_str=rev_str*10+remainder    ## us remainder ko maine add krta jaa rha hu ( actually reverse mai likkh na h final remainder ko)
rev_str=str(rev_str)                ## actually rev_str variable ek integer h so iam converting it into a string
fin_str=str(rev_str[::-1])          ## reversing the string 
print(fin_str)                      ## printing the final string
## done
