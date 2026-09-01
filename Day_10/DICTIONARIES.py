Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#DICTIONARIES
data = {'name':'krishna','batch':63,'course':'PFS'}
data['name']
'krishna'
data['batch']
63
>>> data['course']
'PFS'
>>> 63 in data
False
>>> data['age']
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    data['age']
KeyError: 'age'
>>> data.get('age','key is not present')
'key is not present'
>>> data.get('course','key is not present')
'PFS'
>>> data['batch']
63
>>> data['batch']=64
>>> data
{'name': 'krishna', 'batch': 64, 'course': 'PFS'}
>>> data['skills']=['python','mysql','flask']
>>> data
{'name': 'krishna', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask']}
>>> data['age']=21
>>> data
{'name': 'krishna', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21}
>>> data.update({'phno':98432683134,'email':'kkoppara@gitam.in'})
>>> data
{'name': 'krishna', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 98432683134, 'email': 'kkoppara@gitam.in'}
>>> data.pop('age')
21
>>> data
{'name': 'krishna', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 98432683134, 'email': 'kkoppara@gitam.in'}
>>> del data['name']
>>> data
{'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 98432683134, 'email': 'kkoppara@gitam.in'}
>>> data.popitem()
('email', 'kkoppara@gitam.in')
>>> data
{'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 98432683134}
>>> data.popitem()
('phno', 98432683134)
>>> data
{'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask']}
>>> data.clear()
>>> data
{}
