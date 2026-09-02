#str list tuple dict range()
'''for var in seq
       print(var)'''
'''
s = 'Codegnan'
for ch in s:
    if ch in 'aeiouAEIOU':
        print(ch)

'''
#List of numbers and print even and odd number
'''
l = [10,23,30,45,1,3,15,16,18,19,21]
for i in l:
    if i%2==0:
        print(i,"Even")
    else:
        print(i,"Odd")
'''
#Tuple of numbers
'''
marks  = (34,54,13,46,90,45,33,35,100)
for mark in marks:
    if mark > 35:
        print(mark,"Pass")
    else:
        print(mark,"Fail")
'''
#List of followers in set
'''
followers = {'krishna','bala','sai','hareesh','siva','mokshagna'}
for i in followers:
    print(i)
'''
#Seat number
'''
bus = {'s1':'Booked','s2':'Booked','s3':'Available','s4':'Available','s5':'Booked'}
for seat in bus:
    if bus.get(seat) == 'Available':
        print(seat, bus.get(seat))
'''
#range(start,end+1,step,) => (0,nodef,1)
'''
for i in range(1,11):
    print(i)
'''
'''
for i in range(2,51,2):
    print(i,end=' ')
'''
'''
for i in range(1,100,2):
    print(i,end=' ')
'''
'''
for i in range (5,51,5):
    print(i)
'''
n = int (input("Enter the table no: "))
for i in range(1,11):
    print(f'{n} * {i} = {n*i}')