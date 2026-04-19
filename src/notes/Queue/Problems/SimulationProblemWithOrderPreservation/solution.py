# Problem: Implement a task scheduling system that processes tasks in the order they were added
from collections import deque

class TaskQueue:
    def __init__(self):
        self.queue = deque()

    def add_task(self, task):
        """Add task to the system"""
        self.queue.append(task)

    def process_task(self):
        """Process the next task in order"""
        if not self.queue:
            raise IndexError("No tasks to process")
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0


# Example usage:
tasks = TaskQueue()
tasks.add_task("Print Document")
tasks.add_task("Send Email")
tasks.add_task("Backup Files")

print(tasks.process_task())  # Print Document
print(tasks.process_task())  # Send Email
print(tasks.process_task())  # Backup Files