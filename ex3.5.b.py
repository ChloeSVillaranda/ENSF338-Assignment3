import time
import random
import statistics
import heapq
import matplotlib.pyplot as plt


class InefficientPriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        self.heap.append((priority, item))

    def pop(self):
        max_priority = max(self.heap, key=lambda x: x[0])[0]
        max_priority_items = [item for priority, item in self.heap if priority == max_priority]
        max_priority_item = max_priority_items[0]
        self.heap.remove((max_priority, max_priority_item))
        return max_priority_item


class EfficientPriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (-priority, item))

    def pop(self):
        return heapq.heappop(self.heap)[1]


def test_priority_queue(pq_class, nums):
    times = []
    for i in range(100):
        pq = pq_class()
        random.shuffle(nums)
        start_time = time.time()
        for num in nums:
            pq.push(num, num)
        while pq.heap:
            pq.pop()
        end_time = time.time()
        times.append(end_time - start_time)
    return times


nums = list(range(1000))
inefficient_pq_times = test_priority_queue(InefficientPriorityQueue, nums)
efficient_pq_times = test_priority_queue(EfficientPriorityQueue, nums)

plt.plot(inefficient_pq_times, label='Inefficient priority queue')
plt.plot(efficient_pq_times, label='Efficient priority queue')
plt.legend(loc='upper right')
plt.show()

print(f'Minimum time for inefficient priority queue: {min(inefficient_pq_times)}')
print(f'Average time for inefficient priority queue: {statistics.mean(inefficient_pq_times)}')
print(f'Minimum time for efficient priority queue: {min(efficient_pq_times)}')
print(f'Average time for efficient priority queue: {statistics.mean(efficient_pq_times)}')
