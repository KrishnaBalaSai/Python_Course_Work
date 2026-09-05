Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #string
>>> s = ''
>>> s
''
>>> s = 'codegnan'
>>> s
'codegnan'
>>> 'codegnan'+'pfs'
'codegnanpfs'
>>> 'codegnan'*10
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
>>> ' codegnan '*5
' codegnan  codegnan  codegnan  codegnan  codegnan '
>>> ' * '
' * '
>>> ' * '*10
' *  *  *  *  *  *  *  *  *  * '
>>> ' * '*20
' *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * '
>>> ' * ' *20
' *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * '
>>> '_*_*'*20
'_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*'
>>> '*'*10
'**********'
>>> s = 'codegnan'
>>> s[4]
'g'
>>> s(0)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s(0)
TypeError: 'str' object is not callable
>>> s[0]
'c'
>>> s[-1]
'n'
>>> s[-5]
'e'
>>> names = 'krishna bala sai'
>>> names[0]
'k'
>>> names[-4]
' '
>>> #slicing
#formula s[start:end+1]=>s[0:len:1]
names[0:5]
'krish'
names[:5]
'krish'
names
'krishna bala sai'
names[6:11]
'a bal'
names[12:16]
' sai'
names[-1:-8:-1]
'ias ala'
'sai' in names
True
'krishna' in names
True
'bala' not in names
False
'moksha' in names
False
