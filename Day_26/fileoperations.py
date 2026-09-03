# seek is to read next line
'''
file = open('pfs-63.txt','r')
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()
'''
#Recommended Form
'''
with open('pfs-63.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
'''
'''
with open('pfs-63.txt','w') as file:
    file.write("Shifted to Branch-1")
'''
'''
with open('pfs-63.txt','a') as file:
    file.write("Only for Today\n")
'''
with open('pfs-63.txt','a+') as file:
    file.write("Tomorrow Same Branch 5\n")
    file.seek(0)
    print(file.read())