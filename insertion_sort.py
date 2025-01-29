import timeit
import random

def insertion_sort(arr):
  n= len(arr)
  for j in range(1, n):
    key= arr[j]
    i= j-1
    while i >= 0 and arr[i] > key:
      arr[i+1]= arr[i]
      i= i-1
    arr[i+1]= key
  return arr

arr_sized5 = random.sample(range(1, 101),5)
print(arr_sized5)

arr_sized10 = random.sample(range(1, 101),10)

arr_sized20 = random.sample(range(1, 101),20)

arr_sized50 = random.sample(range(1, 101),50)

arr_sized1000 = random.sample(range(1, 1001),1000)

arr_sized5000 = random.sample(range(1, 5001),5000)

arr_sized10000 = random.sample(range(1, 10001),10000)


insertion_time = timeit.timeit('insertion_sort(arr_sized5)', setup='from __main__ import insertion_sort, arr_sized5', number=1000)
print(f"Insertion Sort Time: {insertion_time}")
insertion_time = timeit.timeit('insertion_sort(arr_sized10)', setup='from __main__ import insertion_sort, arr_sized10', number=1000)
print(f"Insertion Sort Time: {insertion_time}")
insertion_time = timeit.timeit('insertion_sort(arr_sized20)', setup='from __main__ import insertion_sort, arr_sized20', number=1000)
print(f"Insertion Sort Time: {insertion_time}")
insertion_time = timeit.timeit('insertion_sort(arr_sized50)', setup='from __main__ import insertion_sort, arr_sized50', number=1000)
print(f"Insertion Sort Time: {insertion_time}")
insertion_time = timeit.timeit('insertion_sort(arr_sized1000)', setup='from __main__ import insertion_sort, arr_sized1000', number=1000)
print(f"Insertion Sort Time: {insertion_time}")
insertion_time = timeit.timeit('insertion_sort(arr_sized5000)', setup='from __main__ import insertion_sort, arr_sized5000', number=1000)
print(f"Insertion Sort Time: {insertion_time}")
insertion_time = timeit.timeit('insertion_sort(arr_sized10000)', setup='from __main__ import insertion_sort, arr_sized10000', number=1000)
print(f"Insertion Sort Time: {insertion_time}")