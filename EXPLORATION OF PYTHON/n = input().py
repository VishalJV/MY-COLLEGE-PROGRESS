n = input().lower()
a = len(n)
sum = 0
if a == 6:
    for i in range (0,a):
        s = n[i-a]
        if s == "0":
            s = 0
        elif s == "1":
            s = 1
        elif s == "2":
            s = 2
        elif s == "3":
            s = 3
        elif s == "4":
            s = 4
        elif s == "5":
            s = 5
        elif s == "6":
            s = 6
        elif s == "7":
            s = 7
        elif s == "8":
            s = 8       
        elif s == "9":
            s = 9
        if s == chr(97):
            s = 10
        elif s == chr(98):
            s = 11
        elif s == chr(99):
            s = 12
        elif s == chr(100):
            s = 13
        elif s == chr(101):
            s = 14
        elif s == chr(102):
            s = 15
        sum += s * (16**(a - (i+1)))
    print(f"{sum:,}")
else:
    print("Valid hexa decimal number")
