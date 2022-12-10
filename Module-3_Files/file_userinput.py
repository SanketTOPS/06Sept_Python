fl=open('hello.txt','a')

stid=input("Enter ID:")
stnm=input("Enter Name:")
stcity=input("Enter City:")

fl.write(f"ID:{stid}\nName:{stnm}\nCity:{stcity}\n")