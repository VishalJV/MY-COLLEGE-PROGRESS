#JKLU's student portal is rolling out a new sign-up page.
#  Before an account is created, the portal rates the password the student types. 
# It looks for four kinds of characters: an uppercase letter, a lowercase letter, a digit, 
# and a special character (anything that is not a letter, digit or space).
#  A password shorter than 8 characters is always WEAK. Otherwise it is STRONG if all four kinds 
# are present, MODERATE if two or three kinds are present, and WEAK if only one kind is present.
#Input: A single line containing the password.
#  Output: Print STRONG, MODERATE or WEAK. Constraints: 1 ≤ length of password ≤ 50
a=str(input("Enter your password :"))
le=len(a)
for v in range(len(a)):
    b=a[v]
    if b in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print()
