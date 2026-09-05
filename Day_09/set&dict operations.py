Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#SET Operations
s = {}
type(s)
<class 'dict'>
s = set()
s = {1,2,3,4,12,324,9876,34,124313224}
s
{1, 2, 3, 324, 4, 34, 124313224, 12, 9876}
s = set()
s
set()
s.add(1)
s.add(12,3)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.add(12,3)
TypeError: set.add() takes exactly one argument (2 given)
s.add(12.3)
s.add(2+4j)
s.add()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s.add()
TypeError: set.add() takes exactly one argument (0 given)
ss
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ss
NameError: name 'ss' is not defined. Did you mean: 's'?
s
{1, 12.3, (2+4j)}
s={1,1,1,1,1,1}
s
{1}
l={10,20,30}
m={1,2,3,4}
l+m
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    l+m
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a={1,2,3,4,5}
b={3,5,7,9}
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a | b
{1, 2, 3, 4, 5, 7, 9}
a & b
{3, 5}
a - b
{1, 2, 4}
a ^ b
{1, 2, 4, 7, 9}
{1}<=a
True
{1,2,3,4}<=a
True
a
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5}<=a
True
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a.isdisjoint(b)
False
a.isdisjoint({9,10})
True
a.union(b)
{1, 2, 3, 4, 5, 7, 9}
a.intersection(b)
{3, 5}
a.issubset(b)
False
a.issuperset(b)
False
a
{1, 2, 3, 4, 5}
5 in a
True
7 in a
False
8 not in a
True
max(a)
5
min(a)
1
sorted(a)
[1, 2, 3, 4, 5]
sum(a)
15
a
{1, 2, 3, 4, 5}
b=a
b
{1, 2, 3, 4, 5}
b.add(12)
b
{1, 2, 3, 4, 5, 12}
a
{1, 2, 3, 4, 5, 12}
c = a.copy()
c.add(12)
c.add(13)
c
{1, 2, 3, 4, 5, 12, 13}
a
{1, 2, 3, 4, 5, 12}
b
{1, 2, 3, 4, 5, 12}
a.add(123)
a
{1, 2, 3, 4, 5, 123, 12}
a.update({16,17,18})
a
{1, 2, 3, 4, 5, 12, 16, 17, 18, 123}
a.pop()
1
a.pop()
2
a
{3, 4, 5, 12, 16, 17, 18, 123}
a.remove(12)
a
{3, 4, 5, 16, 17, 18, 123}
a.remove(12)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.remove(12)
KeyError: 12
a.discard(12)
a.discard(123)
a
{3, 4, 5, 16, 17, 18}
#DICTIONARIES
d = {}
d=dict()
type(d)
<class 'dict'>
d = {'k1':'v1','k2':'v2','k3':'v3'}
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
id(d)
2338551783296
d['k4']='v4'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.3]='flt'
d
{1: 'int', 12.3: 'flt'}
d[2+3j]='com'
d
{1: 'int', 12.3: 'flt', (2+3j): 'com'}
d['str']='sttring'
d
{1: 'int', 12.3: 'flt', (2+3j): 'com', 'str': 'sttring'}
d[{1,2,3,4)]='tuple'
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
d[(1,2,3,4)]='tuple'
d
{1: 'int', 12.3: 'flt', (2+3j): 'com', 'str': 'sttring', (1, 2, 3, 4): 'tuple'}
d={}
d[1]=1
d[2]=12.3
d[3]=12+4j
d[4]='str'
d[5]=[1,2,3,4]
d[6]=(1,2,3)
d[7]={1,2,3}
d[8]={1:1}
d[9]=True
d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
9 in d
True
10 in d
False
>>> 'str' in d
False
>>> d[5]
[1, 2, 3, 4]
>>> d[8]
{1: 1}
>>> d[10]
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    d[10]
KeyError: 10
>>> d.get(10)
>>> d.get(1)
1
>>> d.get('Key is not present")
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> d.get('Key is not present')
...       
>>> d.get("Key is not present")
...       
>>> d.get(10,"Key is not present")
...       
'Key is not present'
>>> d.get(6,"Key is not present")
...       
(1, 2, 3)
>>> d
...       
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[3]=4
...       
>>> d
...       
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[6]=12
...       
>>> d
...       
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: [1, 2, 3, 4], 6: 12, 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[7]=20
...       
>>> d
...       
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: [1, 2, 3, 4], 6: 12, 7: 20, 8: {1: 1}, 9: True}
