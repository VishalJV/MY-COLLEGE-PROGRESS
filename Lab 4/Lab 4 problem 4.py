hr,mi=map(int,input().split(":"))
if mi+15>59:
    hr=hr+1
    mi=mi+15-60
    print(hr,":",mi,sep="")
    if hr>=24:
            print(hr-24,":",mi,sep="")
elif 0<=hr<24  and mi<60:
    print(hr,":",mi+15,sep="")
##this method is more accurate and easy for understanding the core concept so use the down method its okay for using the above method 
# but you need to apply more complex logic and make it somewhat perfect at the boundarys so that there is no error
hr=int(input("Enter the no of hours :"))
mini=int(input("Enter the minutes :"))
hr=hr*60
total=hr+mini+15
hr=total//60
mini=total%60   
if 0<=hr<24 and 10<=mini<=59:
    print(hr,":",mini,sep="")
if hr==24 and mini<10:
    print("00:0",mini,sep="")   
if 0<=hr<24 and mini<10:
    print(hr,":0",mini,sep="") 