'''
greater = lambda a,b:a if a>b else b

print(greater(12,13))
print(greater(50,70))
print(greater(40,20))
print(greater(16,26))

wish = lambda name: f'Welcome to the course {name}'

print(wish("Krishna"))
print(wish("Bala"))
print(wish("Sai"))

iseven = lambda n: "Even" if n%2==0 else "Odd"

print(iseven(45))
print(iseven(18))
print(iseven(17))

avg = lambda a,b,c: (a+b+c)/3

print(avg(4,5,6))
print(avg(30,26,15))
'''
'''
domain = lambda mail:(mail.split('@')[-1]).split('.')[0]

print(domain('krishna@codegnan.com'))
print(domain('krishna@gmail.com'))
print(domain('krishna@outlook.com'))
print(domain('krishna@yahoo.com'))
'''
'''
gst = lambda price : price + price*0.18

print(gst(1000))
print(gst(5000))
print(gst(8000))
'''
'''
prices = [5678, 8765, 5467, 124, 1600, 3000]

res = list(map(lambda price : price + price*0.18, prices))

print(res)
'''
'''
names = ['krishna','bala','sai','kopparapu','hareesh','moksha']

res = list(map(lambda name: name.title(),names))

print(res)
'''
'''
prices = [5678, 8765, 5467, 124, 1600, 3000]

res = list(map(lambda price: price - price*0.3, prices))

print(res)
'''
'''
prices = [5678, 8765, 5467, 124, 1600, 3000]

res = list(filter(lambda price: price>5000, prices))

print(res)
'''
'''
prices = [5678, 8765, 5467, 124, 1600, 3000]

res = list(filter(lambda price: price%2!=0, prices))

print(res)
'''
'''
names = ['krishna','bala','sai','kopparapu','hareesh','moksha']
res = list(filter(lambda name: len (name)>5, names))
print(res)
'''
'''
from functools import reduce
l = [3,367,6,24,124,435,462]
res = reduce(lambda sum,i:sum+i,l)
print(res)

names = ['krishna','bala','sai','kopparapu','hareesh','moksha']
res = reduce(lambda res,i: res+' '+i, names)
print(res)
'''
products = {'sugar':60,
            'salt':50,
            'eggs':90,
            'cooking oil':120,
            'bread':45
            }
print(dict(sorted(products.items())))
print(dict(sorted(products.items(),reverse=(True))))

print(dict(sorted(products.items(),key = lambda i:i[1])))
print(dict(sorted(products.items(),key = lambda i:i[1],reverse=(True))))