Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#List Methods
l = [1,2,,3,4,5]
SyntaxError: invalid syntax
l = [1,,2,3,4,5]
SyntaxError: invalid syntax
l = [1,2,3,4,5]
l = [10,9,6,1,2,3,4]
l
[10, 9, 6, 1, 2, 3, 4]
id(l)
2568170438080
l.append(12)
l
[10, 9, 6, 1, 2, 3, 4, 12]
l.append(14)
l
[10, 9, 6, 1, 2, 3, 4, 12, 14]
id(l)
2568170438080
l.insert(1,13)
l
[10, 13, 9, 6, 1, 2, 3, 4, 12, 14]
l.extend([52,32,42])
l
[10, 13, 9, 6, 1, 2, 3, 4, 12, 14, 52, 32, 42]
id(l)
2568170438080
l[3]
6
l.pop()
42
l
[10, 13, 9, 6, 1, 2, 3, 4, 12, 14, 52, 32]
l.pop()
32
l.pop()
52
l.pop()
14
l.pop(1)
13
l
[10, 9, 6, 1, 2, 3, 4, 12]
l.pop(2)
6
l.remove(4)
l
[10, 9, 1, 2, 3, 12]
del 1[l]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    del 1[l]
TypeError: 'int' object does not support item deletion
dell[1]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dell[1]
NameError: name 'dell' is not defined
del l[1]
l
[10, 1, 2, 3, 12]
l.clear()
l
[]
#BUILT-IN LIST FUNCTIONS
max(l)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    max(l)
ValueError: max() iterable argument is empty
max(l)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    max(l)
ValueError: max() iterable argument is empty
l
[]
l = [10, 13, 9, 6, 1, 2, 3, 4, 12, 14]
l
[10, 13, 9, 6, 1, 2, 3, 4, 12, 14]
max[l]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    max[l]
TypeError: 'builtin_function_or_method' object is not subscriptable
max(l)
14
min(1)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    min(1)
TypeError: 'int' object is not iterable
min(1)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    min(1)
TypeError: 'int' object is not iterable

min(l)
1
sorted(l)
[1, 2, 3, 4, 6, 9, 10, 12, 13, 14]
l
[10, 13, 9, 6, 1, 2, 3, 4, 12, 14]
sum(l)
74
l.reverse()
l
[14, 12, 4, 3, 2, 1, 6, 9, 13, 10]
l.sort()
l
[1, 2, 3, 4, 6, 9, 10, 12, 13, 14]
l.sort(reverse=True)
l
[14, 13, 12, 10, 9, 6, 4, 3, 2, 1]
l = [1,2,3]
m = [1,2,3]
l
[1, 2, 3]
m
[1, 2, 3]
n = l
m.append(4)
n.append(4)
n
[1, 2, 3, 4]
l
[1, 2, 3, 4]
m.append(10)
m
[1, 2, 3, 4, 10]
m
[1, 2, 3, 4, 10]
l
[1, 2, 3, 4]
all([0,'',[],(),seat(),{},False])
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    all([0,'',[],(),seat(),{},False])
NameError: name 'seat' is not defined. Did you mean: 'set'?
all([0,'',[],(),set(),{},False])
False
>>> any([0,'',[],(),seat(),{},False])
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    any([0,'',[],(),seat(),{},False])
NameError: name 'seat' is not defined. Did you mean: 'set'?
>>> any([0,'',[],(),set(),{},False])
False
>>> l
[1, 2, 3, 4]
>>> l.index(3)
2
>>> l.index(5)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    l.index(5)
ValueError: 5 is not in list
>>> l
[1, 2, 3, 4]
>>> l.count()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    l.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> l.count(3)
1
>>> l.count(5)
0
>>> l
[1, 2, 3, 4]
>>> l = [[1,2,3,4],[5,6,7,8]]
>>> l
[[1, 2, 3, 4], [5, 6, 7, 8]]
>>> l[0]
[1, 2, 3, 4]
>>> l[1]
[5, 6, 7, 8]
>>> l[-1]
[5, 6, 7, 8]
>>> l[0][2]
3
>>> l[1][3]
8
>>> l[-1][-1]
8
>>> #TUPLES
