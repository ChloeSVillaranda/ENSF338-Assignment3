import sys

lst = []
prev_capacity = sys.getsizeof(lst)

for i in range(64):
    lst.append(i)
    new_capacity = sys.getsizeof(lst)
    if new_capacity != prev_capacity:
        print(f"Capacity changed from {prev_capacity} bytes to {new_capacity} bytes at index {i}")
        prev_capacity = new_capacity
