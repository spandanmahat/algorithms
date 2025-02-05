import timeit
import random

#new one
def f(n):
  x = 1
  y = 1
  for i in range(1, n+1):
    for j in range(1, n+1):
      x += 1
      y = i + j
  return x



f_time = timeit.timeit('f(1)', setup='from __main__ import f', number=1000)
print(f"function f(1) Time: {f_time}")
f_time = timeit.timeit('f(2)', setup='from __main__ import f', number=1000)
print(f"function f(2) Time: {f_time}")
f_time = timeit.timeit('f(3)', setup='from __main__ import f', number=1000)
print(f"function f(3) Time: {f_time}")
f_time = timeit.timeit('f(10)', setup='from __main__ import f', number=1000)
print(f"function f(10) Time: {f_time}")

f_time = timeit.timeit('f(50)', setup='from __main__ import f', number=1000)
print(f"function f(50) Time: {f_time}")

f_time = timeit.timeit('f(100)', setup='from __main__ import f', number=1000)
print(f"function f(100) Time: {f_time}")
f_time = timeit.timeit('f(200)', setup='from __main__ import f', number=1000)
print(f"function f(200) Time: {f_time}")
f_time = timeit.timeit('f(500)', setup='from __main__ import f', number=1000)
print(f"function f(500) Time: {f_time}")
f_time = timeit.timeit('f(1000)', setup='from __main__ import f', number=1000)
print(f"function f(1000) Time: {f_time}")
# f_time = timeit.timeit('f(5000)', setup='from __main__ import f', number=1000)
# print(f"function f(5000) Time: {f_time}")
# f_time = timeit.timeit('f(10000)', setup='from __main__ import f', number=1000)
# print(f"function f(10000) Time: {f_time}")