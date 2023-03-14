import time
import random
import statistics
import matplotlib.pyplot as plt

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def test_search(search_fn, arr):
    times = []
    for i in range(100):
        target = random.randint(0, len(arr) - 1)
        start_time = time.time()
        search_fn(arr, target)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

arr = list(range(10000))

linear_search_times = test_search(linear_search, arr)
binary_search_times = test_search(binary_search, arr)

plt.plot(linear_search_times,  label='Linear search')
plt.plot(binary_search_times,  label='Binary search')
plt.legend(loc='upper right')
plt.show()

print(f'Minimum time for linear search: {min(linear_search_times)}')
print(f'Average time for linear search: {statistics.mean(linear_search_times)}')
print(f'Minimum time for binary search: {min(binary_search_times)}')
print(f'Average time for binary search: {statistics.mean(binary_search_times)}')
