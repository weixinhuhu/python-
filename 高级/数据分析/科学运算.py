import time
import math
import numpy as np

# x = [i * 0.001 for i in range(1000000)]
# start = time.perf_counter()
# for i, t in enumerate(x):
#     x[i] = math.sin(t)
# print("math.sin:", time.perf_counter() - start)
#
# x = [i * 0.001 for i in range(1000000)]
# x = np.array(x)
# start = time.perf_counter()
# np.sin(x,x)
# print("numpy.sin:", time.perf_counter() - start)
#
# x = [i * 0.001 for i in range(1000000)]
# start = time.perf_counter()
# for i, t in enumerate(x):
#     x[i] = np.sin(t)
# print("numpy.sin loop:", time.perf_counter() - start)


# y = x1 + x2:	add(x1, x2 [, y])
# y = x1 - x2:	subtract(x1, x2 [, y])
# y = x1 * x2:	multiply (x1, x2 [, y])
# y = x1 / x2:	divide (x1, x2 [, y]), 如果两个数组的元素为整数，那么用整数除法
# y = x1 / x2:	true divide (x1, x2 [, y]), 总是返回精确的商
# y = x1 // x2:	floor divide (x1, x2 [, y]), 总是对返回值取整
# y = -x:	negative(x [,y])
# y = x1**x2:	power(x1, x2 [, y])
# y = x1 % x2:	remainder(x1, x2 [, y]), mod(x1, x2, [, y])
a = np.arange(0,4)
print(a)
b = np.arange(1,5)
print(b)
print("a+b: ", np.add(a, b))
print("a-b: ", np.subtract(a, b))
print("a*b: ", np.multiply(a, b))
print("a/b: ", np.divide(a, b))
print("a/b: ", np.true_divide(a, b))
print("a//b: ", np.floor_divide(a, b))
print("x1**x2: ", np.power(a, b))
print("x1 % x2: ", divmod(a, b))