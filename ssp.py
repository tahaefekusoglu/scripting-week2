from scrp import *

diziler= [
['ali', 'veli', 'hasan', 'cemal', 'sıla', 'damla'],
['hasan', 'cemal', 'sıla', 'damla'],
['sıla', 'damla'],
['ali', 'veli', 'hasan', 'ali', 'veli', 'hasan', 'cemal', 'sıla'],
['ali', 'veli', 'hasan', 'cemal', 'sıla', 'damla']
]

for i in diziler:
    abc = irem(i)
    print(abc)
    rsi(abc)


import random
while True:
    r = random.randint(1, 100)
    rsi(r)
