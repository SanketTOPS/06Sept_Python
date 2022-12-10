fl=open('hello.txt','r+')

#print(fl.read())
#print(fl.readline())
#print(fl.readlines())
#print(fl.readlines()[2])

"""if fl.readable():
    print('Yes...')
else:
    print("Error...")"""

"""n=1
for i in fl:
    #print(i)
    print(f"Line:{n} = {i}")
    n+=1"""


print(fl.read())
fl.write("\nHello Python")
fl.close()