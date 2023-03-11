import json
import time
import matplotlib.pyplot as plt

# Load the array from the ex2data.json file
with open('ex2data.json', 'r') as f:
    array = json.load(f)

# Load the list of search tasks from the ex2tasks.json file
with open('ex2tasks.json', 'r') as f:
    search_tasks = json.load(f)

def binary_search(array, value, start=0, end=None, first_midpoint=None):
    if end is None:
        end = len(array) - 1

    if first_midpoint is not None:
        midpoint = first_midpoint
    else:
        midpoint = (start + end) // 2

    if start > end:
        return None
    elif array[midpoint] == value:
        return midpoint
    elif array[midpoint] < value:
        return binary_search(array, value, midpoint + 1, end)
    else:
        return binary_search(array, value, start, midpoint - 1)


# Create empty lists to store the search values and chosen midpoints
search_values = []
chosen_midpoints = []

# Loop over each search task
for task in search_tasks:
    # Get the search value and the range of valid midpoints
    search_value = task['value']
    midpoint_range = task['midpoint_range']

    # Time the performance of each midpoint in the range
    best_time = float('inf')
    best_midpoint = None
    for midpoint in range(*midpoint_range):
        start_time = time.time()
        result = binary_search(array, search_value, first_midpoint=midpoint)
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Update the best midpoint if this one is faster
        if elapsed_time < best_time:
            best_time = elapsed_time
            best_midpoint = midpoint

    # Append the search value and best midpoint to the lists
    search_values.append(search_value)
    chosen_midpoints.append(best_midpoint)

# Create a scatterplot of search values and chosen midpoints
plt.scatter(search_values, chosen_midpoints)
plt.xlabel('Search Value')
plt.ylabel('Chosen Midpoint')
plt.title('Best Midpoints for Search Tasks')
plt.show()
