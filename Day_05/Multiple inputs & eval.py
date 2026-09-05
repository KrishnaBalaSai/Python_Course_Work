Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#int
X = input()
fgdhggref
X
'fgdhggref'
name = input()
sai
name
'sai'
name = input("Enter your name :")
Enter your name :Krishna Bala Sai
name
'Krishna Bala Sai'
Age = input()
21
Age
'21'
age = input("Enter the age :")
Enter the age :21
age
'21'
age = int(input("Enter the age :"))
Enter the age :21
age
21
type(age)
<class 'int'>
names = input("Enter the names:")
Enter the names:Krishna Bala Sai
names
'Krishna Bala Sai'
names.split()
['Krishna', 'Bala', 'Sai']
names = input("enter the names:").split()
enter the names:Krishna Sai Bala Sai
names
['Krishna', 'Sai', 'Bala', 'Sai']
names = input("Enter the names:").split()
Enter the names:1 2 3 4 5 6 7 8 9
names
['1', '2', '3', '4', '5', '6', '7', '8', '9']
map(int,names)
<map object at 0x00000281A370BD00>
list(map(int,names))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
values = list(map(int,input().split()))
1 2 3 4 5 6 7 8 9 5525 78
values
[1, 2, 3, 4, 5, 6, 7, 8, 9, 5525, 78]
values = list(map(float,input().split()))
12 54 8 845 74
values
[12.0, 54.0, 8.0, 845.0, 74.0]
names = tuple(input()("Enter the names:").split())
Krishna Bala Sai Krishna Sai Bala 
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    names = tuple(input()("Enter the names:").split())
TypeError: 'str' object is not callable
names = tuple(input("Enter the names:").split())
Enter the names:Krishna Bala Sai Krishna Sai Bals
names
('Krishna', 'Bala', 'Sai', 'Krishna', 'Sai', 'Bals')
names = tuple(map(float,input().split()))
4631 684 68635 4
names
(4631.0, 684.0, 68635.0, 4.0)
names = set(input().split())
 12 5 3 4 6
names
{'3', '12', '6', '5', '4'}
a,b = [1,2]
a
1
b
2
a,b = (1,2)
a
1
b
2
email,password = input("Enter the email and password:").split()
Enter the email and password:kkoppara@gitam.in 363635
email
'kkoppara@gitam.in'
password
'363635'
name,marks = input().split
()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    name,marks = input().split
TypeError: cannot unpack non-iterable builtin_function_or_method object
>>> name,marks = input().split()
sai 100
>>> name
'sai'
>>> marks
'100'
>>> int(marks)
100
>>> a,b,c = list(map(int,input().split()))
1 5 2
>>> a
1
>>> b
5
>>> c
2
>>> #eval-we can take all the
>>> e = eval(input())
1
>>> e
1
>>> e = eval(input())
25.558
>>> e
25.558
>>> e = eval(input())
... [1 2 3 4 5]
SyntaxError: multiple statements found while compiling a single statement
>>> e = eval(input())
... [1,2,3,4,5]
SyntaxError: multiple statements found while compiling a single statement
>>> e = eval(input())
[1,2,3,4,5]
>>> e
[1, 2, 3, 4, 5]
>>> e = eval(input())
{1,2,3,45,46}
>>> e
{1, 2, 3, 45, 46}
>>> e = eval(input())
"Krishna Bala Sai"
>>> e
'Krishna Bala Sai'
