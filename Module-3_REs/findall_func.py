import re

mystr="This is Python!"

x=re.findall("is",mystr)
print(x)

if x: #true
    print("Match done...")
else:
    print("Error!")