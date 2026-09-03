'''
n = int(input("Enter the values: "))
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()
'''
'''
n = int(input('Enter the values: '))
for i in range(n):
    for space in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
'''
'''
n = int(input('Enter the values: '))
for i in range(n):
    for space in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()
'''

'''
n = int(input('Enter the values: '))
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or j== n-1 or i== n//2 or j== n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''
#Alphabet A:
'''
n = int(input('Enter the values: '))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet:B
'''
n = int(input('Enter the values: '))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2 or j==n-1 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet c:
'''
n = int(input('Enter the values: '))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet E:
'''n = int(input('Enter the values: '))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet F:
'''
n = int(input('Enter the values: '))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet G:
'''
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 and j<=m or j==m and i>=m or i==m and j>=m or j==n-1 and i>=m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet H:
'''
n=int(input('Enter the values: '))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet I:
'''
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet J:
'''
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2 or j<m and i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet K
'''
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==m and j<=m or i+j==n-1 and i<=m or i==j and i>=m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet L:
'''
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet M
'''
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i+j==n-1 and i<=m or i==j and i<=m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#Alphabets N:
'''
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet O:
'''
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet P:
'''
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2 or j==n-1 and i<n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet Q:
'''
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==n-2 and j==n+2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet R:
'''
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 and i<n//2 or i==n//2 or i==j and i>=m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet S:
'''
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n//2 or i==n-1 or j==0 and i<m or j==n-1 and i>m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet T:
'''
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet U:
'''
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#Alphabet V:
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i+j==n-1 or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
''''''
#Alphabet X:
'''
n=int(input('Enter the values: '))
m = n//2
for i in range(n):
    for j in range(n):
        if i+j==n-1 or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''