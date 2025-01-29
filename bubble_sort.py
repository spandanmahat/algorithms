import timeit
import random

def bubble_sort(arr):
  n = len(arr)
  for i in range(n-1):
    swapped = False
    for j in range(n-1, i,-1):
      if arr[j]< arr[j-1]:
        arr[j], arr[j-1]= arr[j-1], arr[j]
        swapped= True
    if not swapped:
      break
  return arr

arr_sized5 = random.sample(range(1, 101),5)
print(arr_sized5)

arr_sized10 = random.sample(range(1, 101),10)

arr_sized20 = random.sample(range(1, 101),20)

arr_sized50 = random.sample(range(1, 101),50)

arr_sized1000 = random.sample(range(1, 1001),1000)

arr_sized5000 = random.sample(range(1, 5001),5000)

arr_sized10000 = random.sample(range(1, 10001),10000)


bubble_time = timeit.timeit('bubble_sort(arr_sized5)', setup='from __main__ import bubble_sort, arr_sized5', number=1000)
print(f"bubble Sort Time: {bubble_time}")
bubble_time = timeit.timeit('bubble_sort(arr_sized10)', setup='from __main__ import bubble_sort, arr_sized10', number=1000)
print(f"bubble Sort Time: {bubble_time}")
bubble_time = timeit.timeit('bubble_sort(arr_sized20)', setup='from __main__ import bubble_sort, arr_sized20', number=1000)
print(f"bubble Sort Time: {bubble_time}")
bubble_time = timeit.timeit('bubble_sort(arr_sized50)', setup='from __main__ import bubble_sort, arr_sized50', number=1000)
print(f"bubble Sort Time: {bubble_time}")
bubble_time = timeit.timeit('bubble_sort(arr_sized1000)', setup='from __main__ import bubble_sort, arr_sized1000', number=1000)
print(f"bubble Sort Time: {bubble_time}")
bubble_time = timeit.timeit('bubble_sort(arr_sized5000)', setup='from __main__ import bubble_sort, arr_sized5000', number=1000)
print(f"bubble Sort Time: {bubble_time}")
bubble_time = timeit.timeit('bubble_sort(arr_sized10000)', setup='from __main__ import bubble_sort, arr_sized10000', number=1000)
print(f"bubble Sort Time: {bubble_time}")