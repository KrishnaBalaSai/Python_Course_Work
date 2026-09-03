'''
Types of arguments
1)position argument: based on the position the argument is passed
2)Keyword argument: The mapping will depend on the key not a position
3)Default argument: We ar setting a default value to that parameter
4)variable length argument: 1)position:*,2)keyword:**
'''
#1)position argument
'''
def display(name,email,password):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display('krishna','krishna@gmail.com','krishna12*')
display('bala12*','bala@gmail.com','bala')
display('sai@gmail.com','sai12*','sai')
'''
#2)Keyword argument
'''
def display(name,email,password):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display(name='krishna',email='krishna@gmail.com',password='krishna12*')
display(password='bala12*',email='bala@gmail.com',name='bala')
display(email='sai@gmail.com',password='sai12*',name='sai')
'''
#3)Default argument
'''
def display(name,email='gmail.com',password=''):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display(name='krishna',email='krishna@gmail.com',password='krishna12*')
display(password='bala12*',name='bala')
display(email='sai@gmail.com',name='sai')
'''
#4)variable length argument
'''
def display(*names):
    print(names)
display('krishna')
display('krishna','bala')
display('krishna','bala','sai')
display('krishna','bala','sai','kopparapu')
'''
def display(**products):
    print(products)
display(bag=5000)
display(bag=5000,book=30)
display(bag=5000,book=30,bottle=300)