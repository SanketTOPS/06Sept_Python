import re

username=input("Enter Username:")

unm_pattern="[A-Z]+[a-z]+[0-9]"

x=re.findall(unm_pattern,username)

if x:
    print("Username is valid!")
else:
    print("Invalid Username.")

