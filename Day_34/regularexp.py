#Regular Expressions
'''
import re
pattern = r'[0-9]'
text = 'codegnan'
res = re.match(pattern,text)
print(res.group() if res else "Pattern not found")
'''
'''
import re
pattern = r'[0-9]'
text = 'codegnan2026'
res = re.search(pattern,text)
print(res.group() if res else "Pattern not found")
'''
'''
import re
pattern = r'[0-9]'
text = 'codegnan 2026 python version3.14'
res = re.findall(pattern,text)
print(res)
'''
'''
import re
pattern = r'[0-9]'
text = 'codegnan 2026 python version3.14'
res = re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())
'''
'''
import re
pattern = r'[0-9]{10}'
text = '9398899352'
res = re.fullmatch(pattern,text)
print(res.group() if res else "Pattern not found")
'''
'''
import re
pattern = r'[,(#]'
text = 'java,python(html#css'
res = re.split(pattern,text)
print(res)
'''
'''
import re 
pattern = r'[a-z]'
text = 'python version 3.14, batch-63'
res = re.sub(pattern,'*',text)
print(res)
'''
'''
import re 
pattern = r'e.t'
text = 'e@t eaat eat eet ett ect Egfhjet hgjeokj'
res = re.findall(pattern,text)
print(res)
'''
'''
import re 
pattern = r'^(91)'
text = '919695599657'
res = re.findall(pattern,text)
print(res)
'''
'''
import re 
pattern = r'0$'
text = '919695599650'
res = re.findall(pattern,text)
print(res)
'''
'''
import re 
pattern = r'to+'
text = 'to tdfghjk too tooo toooooo'
res = re.findall(pattern,text)
print(res)
'''
'''
import re 
pattern = r'([a-zA-Z])*'
text = 'Codegnan Programming'
res = re.findall(pattern,text)
print(res)
'''
'''
import re 
pattern = r'ab+'
text = 'ab abbb a abbbbbbb abbbb'
res = re.findall(pattern,text)
print(res)
'''
'''
import re 
pattern = r't?o'
text = 'too t@o tstlfo tso'
res = re.findall(pattern,text)
print(res)
'''
'''
import re 
pattern = r'91|0'
text = '025589'
res = re.findall(pattern,text)
print(res)
'''
