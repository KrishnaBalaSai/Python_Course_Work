# mkdir is to create a new folder
'''
import os
os.mkdir("demo")
'''
# rmdir is to delete the folder
'''
import os
os.rmdir("demo")
'''
# get the path we use .getcwd()
'''
import os
print(os.getcwd())
'''
'''
import sys
print("start")
sys.exit()
print("end")
'''
# version of our system
'''
import platform
print(platform.system())
print(platform.release())
print(platform.processor())
'''
'''
import math
print(math.pi)
print(math.e)
print(math.sqrt(36))
print(math.pow(2,3))
print(math.ceil(12.00001))
print(math.ceil(12.3))
print(math.ceil(12.6))
print(math.ceil(12.99999999))
print(math.floor(12.0000001))
print(math.floor(12.3))
print(math.floor(12.6))
'''
'''
import math
print(math.fabs(-10))
print(math.factorial(5))
print(math.gcd(8,24))
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))
'''
'''
import random
print(random.randint(1,10))
print(random.randint(1000000,99999999999))
print(random.random())
print(random.uniform(1,6))

l = ['R','P','S']
print(random.choice(l))
print(random.choices(l,k=2))
random.shuffle(l)
print(l)
'''
'''
from collections import Counter
s = 'python programming'
m = 'this is that that is this is is'.split()
l = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,87,654,56,546,1,5,2,8,3,5,7,6,4,8,9,2,4,22,2,1,2,1,2,1,2]
print(Counter(s))
print(Counter(l))
print(Counter(m))
'''
'''
from collections import defaultdict
s = 'python programming'
m = 'this is that that is this is is'.split()
l = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,87,654,56,546,1,5,2,8,3,5,7,6,4,8,9,2,4,22,2,1,2,1,2,1,2]

d = defaultdict(int)
for i in s:
    d[i]+=1
print(d)
'''
'''
from collections import deque
l = deque([])
l.append(10)
l.append(20)
l.append(30)
l.popleft()
l.popleft()
l.append(50)
l.append(70)
l.popleft()
print(l)
'''
'''
from collections import deque
l = deque([])
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(70)
l.pop()
print(l)
'''
'''
from itertools import combinations, permutations
res1 = list(combinations('abc',2))
res2 = list(permutations('abc',2))
['ab','bc','ca']
print(res1)
print(res2)
'''
from itertools import combinations, permutations
res1 = list(combinations('abc',2))
res2 = list(permutations('abc',2))
print([''.join(i) for i in res1])
print([''.join(i) for i in res2])