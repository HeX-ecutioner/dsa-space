"""
Producer-Consumer Problem (Queue-Based Solution)

The Producer-Consumer problem is a classic synchronization problem where:
- PRODUCERS generate data and put it into a shared buffer
- CONSUMERS take data from the buffer and process it

Key constraints:
- Producers must WAIT if the buffer is FULL
- Consumers must WAIT if the buffer is EMPTY
- Access to the buffer must be THREAD-SAFE

Why a QUEUE is mandatory:
- FIFO order must be preserved
- Producers add to the REAR
- Consumers remove from the FRONT

This problem CANNOT be solved efficiently or correctly without a queue.
"""

import threading
import time
from collections import deque

class BoundedBuffer: # Thread-safe bounded buffer using a queue and condition variables
    def __init__(self, capacity):
        self.buffer = deque()
        self.capacity = capacity
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def produce(self, item): # Producer operation
        with self.not_full:
            while len(self.buffer) == self.capacity:
                self.not_full.wait()   # wait if buffer is full

            self.buffer.append(item)  # enqueue
            print(f"Produced: {item}")

            self.not_empty.notify()   # notify a waiting consumer

    def consume(self): # Consumer operation
        with self.not_empty:
            while not self.buffer:
                self.not_empty.wait()  # wait if buffer is empty

            item = self.buffer.popleft()  # dequeue
            print(f"Consumed: {item}")

            self.not_full.notify()     # notify a waiting producer
            return item


def producer(buffer, count): # Producer Thread
    for i in range(count):
        time.sleep(0.5) # simulate production time
        buffer.produce(i)

def consumer(buffer, count): # Consumer Thread
    for _ in range(count):
        time.sleep(1) # simulate consumption time
        buffer.consume()

# Example usage:
if __name__ == "__main__":
    buffer = BoundedBuffer(capacity=3)

    producer_thread = threading.Thread(target=producer, args=(buffer, 5))
    consumer_thread = threading.Thread(target=consumer, args=(buffer, 5))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    print("Producer-Consumer simulation complete.")