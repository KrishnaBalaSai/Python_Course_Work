'''
import re
fullname = input("Enter the full name: ")
pattern = r'^[A-Za-z]{2,25}([A-Za-z]{2,25})+$'
res = re.fullmatch(pattern,fullname)
print("Valid full name" if res else "Invalid full name")

import re
email = input("Enter the email: ")
pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'
res = re.fullmatch(pattern,email)
print("Valid email" if res else "Invalid email")
'''
'''
import re
phonenumber = input("Enter the Phone Number: ")
pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
res = re.fullmatch(pattern,phonenumber)
print("Valid phone number" if res else "Invalid phone number")
'''
'''
import re
password = input("Enter the Password: ")
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
res = re.fullmatch(pattern,password)
print("Valid password" if res else "Invalid password")
'''
'''
import re
username = input("Enter the username: ")
pattern = r'^[A-Za-z0-9](?:[A-Za-z0-9._]{0,28}[A-Za-z0-9_])?$'
res = re.fullmatch(pattern, username)
print("Valid username" if res else "Invalid username")
'''
'''
import re
aadhar = input("Enter the Aadhaar number: ")
pattern = r'^\d{12}$'
res = re.fullmatch(pattern, aadhar)
print("Valid Aadhaar number" if res else "Invalid Aadhaar number")
'''
import re
pan = input("Enter the PAN card number: ")
pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
res = re.fullmatch(pattern, pan)
print("Valid PAN card number" if res else "Invalid PAN card number")