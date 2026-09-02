'''
i=1
while i<=10:
    print(i)
    i+=1
'''
'''
i=10
while i>0:
    print(i)
    i-=1
'''
'''
i=2
while i<=100:
    print(i)
    i+=2
'''
#print even numbers
'''
i=2
while i<=100:
    print(i,end=' ')
    i+=2
'''
#iterate a string
'''
s = 'python programming'
i =len(s)-1
while i>=0:
    print(s[i],end='')
    i-=1
'''
#remove zeros in list of numbers
'''
l = [1,0,0,0,2,3,4,5,56,12,0,12,0,13,0,0,0,15,0]
while 0 in l:
    l.remove(0)
print(l)
'''
#Take a dict we need a product and price of user
'''
d={}
while True:
    product =input("Enter the product name (for exit): ")
    if product == 'exit':
        break
    price =int(input("Enter the price: "))
    d[product] = price
print(d)
'''
'''
d={}
total_bill=0
while True:
    product =input("Enter the product name (for exit): ")
    if product == 'exit':
        break
    price =int(input("Enter the price: "))
    total_bill+= price
    d[product] = price
print(d)
print("Total Bill:",total_bill)
'''
i = 0
while i<=10:
    i+=1
    if i == 15:
        break
    print(i)
else:
    print("End of the loop")