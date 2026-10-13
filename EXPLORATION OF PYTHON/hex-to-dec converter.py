sum=0
num1 = input(("Enter the Hex value ")).upper()
if len(num1)==6:
    for i in range(6):
        char =num1[i] 
        if char == "A":
            val1 = 10
        elif char  == "B":
            val1 = 11
        elif char  ==  "C":
            val1 = 12
        elif  char == "D":
            val1 = 13
        elif char  =="E":
            val1 = 14
        elif char == "F":
            val1 = 15
        elif char == "1":
            val1 = 1
        elif char == "2":
            val1 = 2
        elif char == "3":
            val1 = 3
        elif char == "4":
            val1 = 4
        elif char  =="5":
                val1 = 5
        elif char == "6":
            val1 = 6
        elif char == "7":
            val1 = 7
        elif char == "8":
            val1 = 8
        elif char  =="9":
            val1 = 9
        elif char == "0":     #####   char ends mannn
            val1 = 0  
        sum=val1*(16**(5-i))+sum
    print(f"The Decimal from is {sum}")
else:
    print("ENTER A VALID HEXADECIMAL VALUE")
