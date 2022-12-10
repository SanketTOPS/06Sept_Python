fl=open('test.txt','w')
fl.write("Hello Student")

if fl.writable():
    print("Yes...")
else:
    print("Error...")