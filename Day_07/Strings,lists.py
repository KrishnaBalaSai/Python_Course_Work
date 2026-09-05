Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
c  = 'strinigs.py'
c.startswith('str')
True
c.startswith('python')
False
c.endswith('py')
True
c.endswith('python')
False
c.islower()
True
c.isupper()
False
'PYTHONV13'
'PYTHONV13'
'PYTHONV13'.isupper()
True
c.isaplha()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    c.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
c.isalpha()
False
c.isalnum()
False
'             'isspace()
SyntaxError: invalid syntax
'       '.isspace()
True
'h       '.isspace()
False
'this is python class'.istitle()
False
'This Is Python Class'.istitle()
True
's123'.isalnum()
True
's.123'.isalnum()
False
'my@var'isidentifier()
SyntaxError: invalid syntax
'my@var'.isidentifier()
False
>>> 'my_var'.isidentifier()
True
>>> l = []
>>> l = list()
>>> l = [1,12.3,2+3j,'str',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},None,true]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    l = [1,12.3,2+3j,'str',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},None,true]
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> l = [1,12.3,2+3j,'str',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},None,True]
>>> l
[1, 12.3, (2+3j), 'str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, None, True]
>>> l = [1,1,1,1,1]
>>> l
[1, 1, 1, 1, 1]
>>> type(1)
<class 'int'>
>>> l = [1,2,3,4,5]
>>> m = [5,6,7]
>>> l+m
[1, 2, 3, 4, 5, 5, 6, 7]
>>> m*3
[5, 6, 7, 5, 6, 7, 5, 6, 7]
>>> l
[1, 2, 3, 4, 5]
>>> l[3]
4
>>> 1[-1]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    1[-1]
TypeError: 'int' object is not subscriptable
>>> l[-1]
5
>>> l[1:]
[2, 3, 4, 5]
>>> l[:2]
[1, 2]
>>> 1[::-1]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    1[::-1]
TypeError: 'int' object is not subscriptable
>>> l[::-1]
[5, 4, 3, 2, 1]
