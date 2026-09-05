Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
a//b
2
a%b
0
a**b
10240000000000
#Comparison Operators
a=20
b=35
a<b
True
a<b
True
a>b
False
a<=b
True
a>=b
False
a==b
False
a!=b
True
#Assignment Operators
a=23
a+=20
a
43
a-+24
19
a*=9
a
387
a//=5
a
77
a/=2
a
38.5
a**=2
a
1482.25
a%=3
a
0.25
#Relational Operators
#Relational Operators
a=20
a%2==0
True
a%3==0
False
a%2 and a%3 ==0
0
a%2==0 and a%3==0
False
a%2==0 or a%3==0
True
not a<6
True
a=45
not a<44
True
a<44
False
not a<4
True
not a>43
False
#Membership Operators
s='Codegnan'
'e' in s
True
'r' in s
False
'i' not in s
True
'e' not in s
False
l=[1,2,3,4,5,6,7]
5 in l
True
8 in l
False
t=(4,5,6,7,9,'sai','hill')
'sail' in t
False
'hill' in t
True
'sai'not in t
False
s={1,2,4,5,6,8}
1 in s
True
1 not in 4
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    1 not in 4
TypeError: argument of type 'int' is not iterable
1 not in s
False
d={'day':'Monady','date':12}
'day' in d
True
'week' in d
False
12 in d #values aren't count
False
#Identity Operators
#It checks whether both the objects or variables are sharing the same memory location or not.
a=[1,2,3,4,5]
b=[6,7,8,9,0]
id(a)
1566963208000
id(b)
1566963419840
a is b
False
a = b
a is b
True
n=t
id(t)
1566958123712
a=t
id(t)
1566958123712
t=a
id(t)
1566958123712
m=b
id(m)
1566963419840
#The major difference b/w the mutable and immutable data types is, in Mutable we can change the elements in the data type within the same memory allocation but in immutable we can't.
#Or (Interview level)Mutable data types allow you to change their elements after creation without creating a new object. Immutable data types do not allow modification; any change results in the creation of a new object.
#Bitwise operators
9&10
8
9}10
SyntaxError: unmatched '}'
9|10
11

9^10
3
8>>2
2
8<<3
64
~8
-9
~12
-13
~45
-46
>>> #Output stmts
>>> a=10
>>> b=10.54
>>> c='Codegnan'
>>> print(a,b,c)
10 10.54 Codegnan
>>> print("a value is",a)
a value is 10
>>> print("a value is",a,"| b value is",b,"|c value is",c)
a value is 10 | b value is 10.54 |c value is Codegnan
>>> print(a,b,c)
10 10.54 Codegnan
>>> print(a,b,c,sep='')
1010.54Codegnan
>>> print(a,b,c,sep="\t")
10	10.54	Codegnan
>>> print(a,b,c,sep=",",end='\n')
10,10.54,Codegnan
>>> print(a,b,c,sep=",",end='\n\n')
10,10.54,Codegnan

>>> print(a,b,c,sep=",",end='@')
10,10.54,Codegnan@
>>> print(f'a={a} b={b} c={c}')
a=10 b=10.54 c=Codegnan
>>> print(f'a=%d b=%.4f c=%s')
a=%d b=%.4f c=%s
>>> print(f'a=%d b=%.4f c=%s'%(a,b,c))
a=10 b=10.5400 c=Codegnan
>>> print(f'a={} | b={} | c={}'.format(c,b,a))
SyntaxError: f-string: empty expression not allowed
>>> print('a={} | b={} | c={}'.format(c,b,a))
a=Codegnan | b=10.54 | c=10
>>> print('a={} | b={5} | c={}'.format(c,b,a))
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    print('a={} | b={5} | c={}'.format(c,b,a))
ValueError: cannot switch from automatic field numbering to manual field specification
>>> print('a={} | b={2} | c={}'.format(c,b,a))
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    print('a={} | b={2} | c={}'.format(c,b,a))
ValueError: cannot switch from automatic field numbering to manual field specification
>>> print('a={1} | b={2} | c={0}'.format(a,b,c))
a=10.54 | b=Codegnan | c=10
