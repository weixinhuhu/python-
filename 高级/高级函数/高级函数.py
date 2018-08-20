l1=["wangwang","tongtong"]
l2=[89,100]
z=zip(l1,l2)
l3=[i for i in z]
print(l3)

import collections
# help(collections.namedtuple)
Point=collections.namedtuple("point",['x','y'])
p=Point(22,33)
print(p.x)
print(p[0])

Circle=collections.namedtuple("Circle",['x','y','r'])
c=Circle(100,150,50)
print(c)

from collections import deque
q=deque(['a','b','v'])
print(q)
q.append("d")
print(q)
q.appendleft("pp")
print(q)

from  collections import defaultdict
func=lambda :"null"
d=defaultdict(func)
d["one"]=1
d["two"]=2
print(d["one"])
print(d["four"])

from collections import Counter
c=Counter("wqweqwewqeqwewqeweqwrqrqwrqwrwqrqwr")
print(c)

s=["love","you","TTLY","love","ttly"]
c=Counter(s)
print(c)

