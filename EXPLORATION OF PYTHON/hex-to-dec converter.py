print("This is a Converter ")
num1 = input(("Enter the Hex value "))
first_char =num1[0] 
second_char =num1[1]

if first_char == "A":
    first_val1 = 10
if first_char  == "B":
    first_val1 = 11
if first_char  ==  "C":
    first_val1 = 12
if  first_char == "D":
 first_val1 = 13
if first_char  =="E":
  first_val1 = 14
if first_char == "F":
    first_val1 = 15
if first_char == "1":
   first_val1 = 1
if first_char == "2":
   first_val1 = 2
if first_char == "3":
   first_val1 = 3
if first_char == "4":
   first_val1 = 4
if first_char  =="5":
   first_val1 = 5
if first_char == "6":
  first_val1 = 6
if first_char == "7":
    first_val1 = 7
if first_char == "8":
    first_val1 = 8
if first_char  =="9":
    first_val1 = 9
if first_char == "0":##### first char ends
   first_val1 = 0  
if second_char  =="A":
    second_val1 =10
if second_char  =="B":
     second_val1 =11
if second_char =="C":
     second_val1 =12
if  second_char == "D":
   second_val1 =13
if second_char =="E":
     second_val1 =14
if second_char == "F":
    second_val1 =15   
if second_char == "1":
     second_val1 =1
if second_char =="2":
     second_val1 =2
if second_char =="3":
     second_val1 =3
if second_char =="4":
     second_val1 =4
if second_char =="5":
  second_val1 =5
if second_char =="6":
     second_val1 =6
if second_char =="7":
   second_val1 =7
if second_char =="8":
    second_val1 =8
if second_char =="9":
     second_val1 =9
if second_char =="0":
    second_val1 =0   
print(16*first_val1+second_val1)