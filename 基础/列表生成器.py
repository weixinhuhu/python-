L1 = ['Hello', 'World', 18, 'Apple', None]

L2=L1
print(L2)

L2.append("112233")
print(L1,id(L1))
print(L2,id(L2))

L2=[s.lower() for s in L1]
print(L2)

L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)
