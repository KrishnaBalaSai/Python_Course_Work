# Function is a block of reusable code
'''
def display(name,email,password):
    print(f'Hello {name},')
    print(f'your email {email},')
    print(f'your password {password}')
display('krishna','krishna@gmail.com','krishna12*')
display('Bala','bala@gmail.com','bala12*')
display('sai','sai@gmail.com','sai12*')
'''
#leap year or not
'''
def isleapyear(year):
    if year%400 == 0 or (year%4 == 0 and year%100!=0):
        print(f"{year}is leap year")
    else:
        print(f"{year}is not a leap year")
for year in range(2001,2027):
    isleapyear(year)
'''
#Sum of digits
'''
def sumofdigits(n):
    sum = 0
    while n>0:
        sum += n%10
        n=n//10
    return sum
n = int(input("Enter the number: "))
print(f'sum of {n} digits is {sumofdigits(n)}')
'''
#multiplication od digits
'''
def productofdigits(n):
    pro = 1
    while n>0:
        pro *= n%10
        n=n//10
    return pro
n = int(input("Enter the number: "))
print(f'product of {n} digits is {productofdigits(n)}')
'''
#password
'''
def checkpassword(password):
    if len(password) > 8:
        check = set()
    for i in password:
        if i.isupper():
            check.add('u')
        elif i.islower():
            check.add('l')
        elif i.isdigit():
            check.add('d')
        else:
            check.add('s')
    if len(check) == 4:
        return "strong Password"

    return "Weak Password"
password = input("Enter the password:")
print(f'password is {checkpassword(password)}')
'''

#Tables
def table(n):
    print(f'--------------------------Table - {n}---------------------------')
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')
for i in range(1,21):
    table(i)