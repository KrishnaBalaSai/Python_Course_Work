#Recursions
'''
def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(1)
'''
'''
def display(n):
    if n>10:
        return
    display(n+1)
    print(n)
display(1)
'''
#find sum of N numbers using recursions
'''
def displaysum(n):
    if n==0:
        return 0
    return n + displaysum(n-1)
print(displaysum(8))
'''
#find the product of N numbers using recursions
'''
def displayprod(n):
    if n==1:
        return 1
    return n * displayprod(n-1)
print(displayprod(5))
'''
#using recursion display the String
'''
def display(ind):
    if ind == len(s):
        return
    print(s[ind],end=' ')
    display(ind+1)

s = 'python programming'
display(0)
'''
'''
def display(n):
    if n > len(s):
        return
    print(s[:n])
    display(n+1)
s = 'python programming'
display(1)
'''
'''
def display(ind,w):
    if ind > len(s)-w:
        return
    print(s[ind:ind+w])
    display(ind+1,w)
s = 'python programming'
display(0,10)
'''
'''
def display(n):
    if n == 0:
        return
    display(n//10)
    print(n%10)
n = 987654
display(n)
'''
'''
def display(n):
    if n == 0:
        return 0
    return n%10 + display(n//10)
n = 987654
print(display(n))
'''
a =0
b = 1
n = 10
for i in range(n-1):
    a,b = b,a+b
    print(b)