email = input("What's your email: ").strip()
# strip take whitespaces after and before the text.

'''
if "@" and "." in email:
     print("Valid")
else:
     print("Invalid")
'''

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

