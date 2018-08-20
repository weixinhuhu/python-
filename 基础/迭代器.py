def findMinAndMax(L):
    if L == []:
        return(None,None)
    else:
        min = L[0]
        max = L[0]
        for i in L:
            if min > i:
                min = i
            if max < i:
                max = i
    return (min, max)

def findMinAndMax_1(L):
    if L == []:
        return (None, None)
    else:
        return (min(L), max(L))

if findMinAndMax_1([]) != (None, None):
    print('测试失败!')
elif findMinAndMax_1([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax_1([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax_1([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
