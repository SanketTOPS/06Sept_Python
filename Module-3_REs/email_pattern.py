import re

#sanket_chauhan@gmail.com
email=input("Enter an email:")

email_pattern="^[a-z0-9._]+[@]+[a-z]+[\.]+[a-z]{2,}$"

x=re.findall(email_pattern,email)

if x:
    print("Valid Email!")
else:
    print("Invalid Email!")