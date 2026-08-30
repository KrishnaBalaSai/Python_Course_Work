Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Methods in string
c = 'python programming'
len(c)
18
ord('p')
112
ord('a')
97
ord('0')
48
ord('A')
65
chr(65)
'A'
chr(66)
'B'
min(c)
' '
max(c)
'y'
sorted(c)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
chr(50)
'2'
c = 'String is immutable'
c
'String is immutable'
c.upper()
'STRING IS IMMUTABLE'
c.lower()
'string is immutable'
c.title()
'String Is Immutable'
c.captitalize()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    c.captitalize()
AttributeError: 'str' object has no attribute 'captitalize'. Did you mean: 'capitalize'?
c.capitalize()
'String is immutable'
c.swapcase()
'sTRING IS IMMUTABLE'
'STRAẞEMÁLAGAÅngströmCafé'.casefold()
'strassemálagaångströmcafé'
#2. Alignment & Formatting Methods
c = "String Is Immutable"
c
'String Is Immutable'
c.center(60,0)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    c.center(60,0)
TypeError: The fill character must be a unicode character, not int
c.center(60,'0')
'00000000000000000000String Is Immutable000000000000000000000'
c.ljust(60,'-')
'String Is Immutable-----------------------------------------'
c.rjust(60,'-')
'-----------------------------------------String Is Immutable'
'12'.zfill(4)
'0012'
'12'.zfill(6)
'000012'
'12345'.zfill(5)
'12345'
#3. Search & Find Methods
c
'String Is Immutable'
c.find('i')
3
c.find('z')
-1
c.rfind('i')
3
c.rfind('I')
10
c.index('i)
        
SyntaxError: unterminated string literal (detected at line 1)
c.index('i')
        
3
c.rindex('g')
        
5
c.rindex('z')
        
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    c.rindex('z')
ValueError: substring not found
c.count('i')
        
1
c.count('m')
        
2
c.count('z')
        
0
#4. String Testing Methods (Boolean Results)
        
#5. Replace & Modify Methods
        
c = 'String is immutable'
        
c
        
'String is immutable'
c.replace('i','0')
        
'Str0ng 0s 0mmutable'
c.replace('String','Float')
        
'Float is immutable'
c.maketrans('aeiou','12345')
        
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.translate(c.maketrans('aeiou','12345'))
        
'Str3ng 3s 3mm5t1bl2'
#6. Splitting & Joining Methods
        
c
        
'String is immutable'
c.split()
        
['String', 'is', 'immutable']
'string,is,immutable'
        
'string,is,immutable'
'string,is,immutable'.split()
        
['string,is,immutable']
'string,is,immutable'.split(',')
        
['string', 'is', 'immutable']
c.rsplit()
        
['String', 'is', 'immutable']
c.rsplit(',')
        
['String is immutable']
c.rsplit(',',1)
        
['String is immutable']
'string is immutable'rsplit(','1)
        
SyntaxError: invalid syntax
'string is immutable'.rsplit(','1)
        
SyntaxError: invalid syntax. Perhaps you forgot a comma?
'string is immutable'.rsplit(',',1)
        
['string is immutable']
s = '''
python
programming
lang
'''
        
s
        
'\npython\nprogramming\nlang\n'
s.splitlines()
        
['', 'python', 'programming', 'lang']
['', 'python', 'programming', 'lang'].join()
        
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    ['', 'python', 'programming', 'lang'].join()
AttributeError: 'list' object has no attribute 'join'
join(['', 'python', 'programming', 'lang'])
        
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    join(['', 'python', 'programming', 'lang'])
NameError: name 'join' is not defined
''.join(['', 'python', 'programming', 'lang'])
        
'pythonprogramminglang'
' '.join(['', 'python', 'programming', 'lang'])
        
' python programming lang'
'-'.join(['', 'python', 'programming', 'lang'])
        
'-python-programming-lang'
'.'.join([,2,3])
        
SyntaxError: invalid syntax
','.join([,2,3])
        
SyntaxError: invalid syntax
'python.py'.partition(',')
        
('python.py', '', '')
'python.py'.partition('.')
        
('python', '.', 'py')
s = 'java,python,c,c++'
        
s
        
'java,python,c,c++'
>>> s.partition(',')
...         
('java', ',', 'python,c,c++')
>>> s.rpartition(',')
...         
('java,python,c', ',', 'c++')
>>> #7. Whitespace & Trimming Methods
...         
>>> c = 'Hello world'
...         
>>> c
...         
'Hello world'
>>> c.strip()
...         
'Hello world'
>>> c = ' Hello world '
...         
>>> c,strip()
...         
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    c,strip()
NameError: name 'strip' is not defined
>>> c.strip()
...         
'Hello world'
>>> c.lstrip()
...         
'Hello world '
>>> c.rstrip()
...         
' Hello world'
>>> #8. Encoding & Decoding Methods
...         
>>> text ="Hello 🙂"
...         
>>> text
...         
'Hello 🙂'
>>> text.encode()
...         
b'Hello \xf0\x9f\x99\x82'
>>> b'Hello \xf0\x9f\x99\x82'.decode()
...         
'Hello 🙂'
