import threading
import random
import time

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def enqueue(self, data):
        while True:
            self.lock()
            if ((self.tail + 1) % self.size == self.head):
                # Queue is full, wait for one second and try again
                self.unlock()
                time.sleep(1)
            else:
                if (self.head == -1):
                    # First element in the queue
                    self.head = 0
                    self.tail = 0
                    self.queue[self.tail] = data
                else:
                    self.tail = (self.tail + 1) % self.size
                    self.queue[self.tail] = data
                self.unlock()
                return

    def dequeue(self):
        while True:
            self.lock()
            if (self.head == -1):
                # Queue is empty, wait for one second and try again
                self.unlock()
                time.sleep(1)
            else:
                dequeued_data = self.queue[self.head]
                if (self.head == self.tail):
                    # Last element in the queue
                    self.head = -1
                    self.tail = -1
                else:
                    self.head = (self.head + 1) % self.size
                self.unlock()
                return dequeued_data

def producer():
    while True:
        # Generate a random number between 1 and 10
        num = random.randint(1, 10)
        
        # Wait for that many seconds
        time.sleep(num)
        
        # Enqueue the number to the queue
        q.lock()
        if ((q.tail + 1) % q.size == q.head):
            print("Queue is full. Producer is waiting.")
            q.unlock()
            continue
        elif (q.head == -1):
            q.head = q.tail = 0
        else:
            q.tail = (q.tail + 1) % q.size
        q.queue[q.tail] = num
        print(f"Producer enqueued {num}")
        q.unlock()

def consumer():
    while True:
        # Generate a random number between 1 and 10
        num = random.randint(1, 10)
        
        # Wait for that many seconds
        time.sleep(num)
        
        # Dequeue a number from the queue
        q.lock()
        if (q.head == -1):
            print("Queue is empty. Consumer is waiting.")
            q.unlock()
            continue
        else:
            dequeued_num = q.queue[q.head]
            if (q.head == q.tail):
                q.head = q.tail = -1
            else:
                q.head = (q.head + 1) % q.size
            print(f"Consumer dequeued {dequeued_num}")
        q.unlock()


if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()