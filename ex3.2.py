import json
import time
import matplotlib.pyplot as plt

# Load the array from the ex2data.json file
with open('ex2data.json', 'r') as f:
    array = json.load(f)

# Load the list of search tasks from the ex2tasks.json file
with open('ex2tasks.json', 'r') as f:
    search_tasks = json.load(f)

# Define the tweaked binary search function
def binary_search(array, target, start_midpoint=None):
    low = 0
    high = len(array) - 1

    if start_midpoint is not None and start_midpoint >= 0 and start_midpoint <= high:
        mid = start_midpoint
    else:
        # Start the search from the middle of the array
        mid = len(array) // 2

    while low <= high:
        if array[mid] == target:
            return True
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    return False

# Time the performance of each search task using the tweaked binary search with midpoints at 1/5, 2/5, 3/5, and 4/5 of the array
results = []

for task in search_tasks:
    best_midpoint = None
    best_time = float('inf')
    found = False

    midpoints = [len(array)//5, 2*len(array)//5, 3*len(array)//5, 4*len(array)//5]

    for mid in midpoints:
        start_time = time.perf_counter()
        result = binary_search(array, task, start_midpoint=mid)
        end_time = time.perf_counter()

        if end_time - start_time < best_time:
            best_time = end_time - start_time
            best_midpoint = mid/len(array)

        if result:
            found = True
            break

    results.append((task, best_midpoint, found, best_time))

for task in search_tasks:
    best_midpoint = None
    best_time = float('inf')
    found = False

    midpoints = [len(array)//5, 2*len(array)//5, 3*len(array)//5, 4*len(array)//5]

    for mid in midpoints:
        start_time = time.perf_counter()
        result = binary_search(array, task, start_midpoint=mid)
        end_time = time.perf_counter()

        if end_time - start_time < best_time:
            best_time = end_time - start_time
            best_midpoint = mid/len(array)

        if result:
            found = True
            break

    results.append((task, best_midpoint, found, best_time))

    print(f"Search for {task}: {'Found' if found else 'Not Found'} (Best Midpoint: {best_midpoint}, Best Time: {best_time:.6f} seconds)")


# Plot a scatterplot of task versus best midpoint
plt.scatter([task for task, midpoint, found, time in results], [midpoint for task, midpoint, found, time in results])
plt.xlabel('Task')
plt.ylabel('Best Midpoint')
plt.title('Task vs Best Midpoint')
plt.show()
