#JKLU's student portal is rolling out a new sign-up page.
#  Before an account is created, the portal rates the password the student types. 
# It looks for four kinds of characters: an uppercase letter, a lowercase letter, a digit, 
# and a special character (anything that is not a letter, digit or space).
#  A password shorter than 8 characters is always WEAK. Otherwise it is STRONG if all four kinds 
# are present, MODERATE if two or three kinds are present, and WEAK if only one kind is present.
#Input: A single line containing the password.
#  Output: Print STRONG, MODERATE or WEAK. Constraints: 1 ≤ length of password ≤ 50
a=str(input("Enter your password :"))                                ## defaultly all the parameters are set to false
uppp=False                              ## defaultly all the parameters are set to false
loww=False                              ## defaultly all the parameters are set to false
spl=False                               ## defaultly all the parameters are set to false
dig=False                               ## defaultly all the parameters are set to false
cnt=0                   #   <------- this is the most important variable you need for this prroblem
if len(a)<8:
    print("WEAK PASS")
else:
    for v in range(len(a)):
        b=a[v]
        if b.isupper():                             ## if upper then true
            uppp=True
        if b in "~!@#$%^&*()_+-=}{[]:''<>?,./|":    ## if special then true
            spl=True
        if b.islower():                             ## if lower then true
            loww=True
        if b.isnumeric():                           ## if digit then true
            dig=True
    cnt = spl + uppp + loww + dig
    if cnt==4 :                                   ## here if all the cases are true then the value becomes 4 
        print("Strong Pass")
    elif cnt<4 :                                  ## here if not all the cases are not satisfied then it becomes <4 so modeate pass 
        print("Moderate Pass")
