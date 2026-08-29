Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
count = 10
count = 7
count
7
type(count)
<class 'int'>
price = 99.99
price
99.99
type(price)
<class 'float'>
c = 3+8j
c
(3+8j)
c = 4+8J
c
(4+8j)
>>> type(c)
<class 'complex'>
>>> #2)Sequence Types
>>> s = 'codegnan'
>>> s
'codegnan'
>>> s = "code"
>>> s
'code'
>>> type(s)
<class 'str'>
>>> l = list()
>>> l
[]
>>> type(l)
<class 'list'>
>>> l = [1,,2,3,4,5,"dfghijk",78.678,[123],[456]}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> l = [1,2,3,4,5,"dfghijk",78.678,[1,2,3},(1,2)]
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> l = [1,2,3,4,5,"fsfaf",75.25,[1,2,3,4],(2,4,5)]
>>> l
[1, 2, 3, 4, 5, 'fsfaf', 75.25, [1, 2, 3, 4], (2, 4, 5)]
>>> type(l)
<class 'list'>
>>> t = (1,2,43,3,5,3,'gfds',23.23,[324],(324))
>>> t
(1, 2, 43, 3, 5, 3, 'gfds', 23.23, [324], 324)
>>> type(t)
<class 'tuple'>
>>> s = {1,2,3,4,5,"wefwd",525.55}
>>> s
{1, 2, 3, 4, 5, 'wefwd', 525.55}
>>> s = {1,2,3,4,5,"wefwd",525.55,"fdvewe"34}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> s = {1,2,3,4,5,"wefwd",525.55,"fdvewe",34}
>>> s
{1, 2, 3, 4, 5, 34, 'fdvewe', 525.55, 'wefwd'}
>>> type(s)
<class 'set'>
>>> dict = {"name":"sai","age":21,"course":"pfs"}
>>> dict
{'name': 'sai', 'age': 21, 'course': 'pfs'}
>>> type(dict)
<class 'dict'>
