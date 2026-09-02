'''
s = 'python programming'
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        print(i,s[i])
'''

#Go with the list
'''
l=[23,45,12,34,50,24,35,68,75,34,10]
for i in range(len(l)):
    print(i,l[i],end=' ')

'''
'''
l=[23,45,12,34,50,24,35,68,75,34,10]
sum=0
for i in range(len(l)):
    if l[i]%2==0:
        sum=sum+i
        print(i,l[i],end=' ')
print(sum)
'''
#Factorial
'''
n = int(input("Enter the number: "))
fact = 1
for i in range(1,n+1):
    fact *= i
print(f"Factorial of {n} is {fact}")
'''
'''
data={}
n = int(input("Enter the no.of students: "))
max_marks = 0
for i in range(n):
    name = input("Enter the name: ")
    marks = int(input("Enter the mark: "))
    if marks > max_marks:
        max_marks = marks
    data[name] = marks
print(data)
print("Maximum Marks:",max_marks)
'''
data={}
total_bill = 0
n = int (input("Enter the no of items: "))
for i in range(n):
    item = input("Enter the item: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))
    final_price = price*quantity
    total_bill += final_price
    data[item] = price
    data[item] = f'{quantity} * {price} = {final_price}'
print(data)
print("Total Bill:",total_bill)
