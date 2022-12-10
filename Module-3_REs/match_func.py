import re

mystr="This is Python!"

x=re.match('Python',mystr)
print(x)

if x: #true
    print("Match done...")
else:
    print("Error!")