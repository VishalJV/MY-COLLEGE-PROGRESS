num1=int(input("number1 ",))
num2=int(input("number2 ",))
num3=int(input("number3 ",))
print(num1+num2+num3)

#ask the user for 5 numbers and priint their avg value
v1=int(input("num1= "))
v2=int(input("num2= "))
v3=int(input("num3= "))
v4=int(input("num4= "))
v5=int(input("num5= "))

print((v1+v2+v3+v4+v5)/5)

eve=int(input("give a number ",))   # if condition taruvatha we use colon : this bcoz python ki telvadi where does the conditioning starts anedi so we use colon
if eve %  2 ==0 :
   print("the given number is even") #ee line lo starting the gap is called identitation many languages lo we us curley braces but in pythpn we use that gap to tell python that this condition is under the rule of the above operation ani 
else :
   print("the given number is odd")
jv =int(input("Enter a number "))
if jv < 7:
   print("the given number is less than  7")
if jv == 7:
   print("the given num is 7")
else :
   print("the given number is above the value of 7")   

mark1=int(input("enter  your marks"))

if mark1>=90:
   print("grade A")
elif mark1>80:
   print("grade B")
else :
   print("grade C")   


x = 1
for i in range(1,11) :
  print(f"9 x {i} = {9*i}")# broo formatted string is very useful in printing tables 
  #printing tables is also asked in interviews in some companys so deal with these care fully
  #whats the point of formatting a string  is Build a sentence where some parts are fixed text, and some parts are dynamic (variables or calculations).
  # “Take the current value of x, add 1 to it, and store it back into x.”  x=x+1


for k in range (1,21) :
  for  l in range(1,11) :
    print(f"{k} x {l}={k*l}")
    print("____")
    #loops concept 
for i in range(5) :
   print("vishal")
    ####ee line lo unna numbers 0 to n-1 untai anthey n count kaadu adi chusko not included the number which had given
    #for example for i in range (5) ani nen code chestey python emi artham cheskuntundi antey 0 1 2 3 4 anthey 5 numbers untai including the number 0 biut not the number n we had given 
# ikkada i anedi kuda oka variable nuvvu daani place lo edaina pettochhu
# for means: "Take each item one by one from a collection and do the same work. for aney padaniki adey meaning undi its imp for knowing the word
#range lo kuda manaki 3 different types kanipisthayi first tyoe enti antey adi already mention chesinna only brackets lo untundi 
# like for i in range(n) :(n anedi oka number genral gaa oka example teeskuna
# ) idi classic example only 0 nundi start avytundi till the number excet the one 
# commas use chesinappudu oak space vastundi ratrher than we use + sign for replacing that
# 
#
#








