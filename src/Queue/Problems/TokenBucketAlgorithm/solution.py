# Problem: Allow at most N requests in a time window of T seconds

from collections import deque
import time

class RateLimiter:
    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window = window_seconds
        self.requests = deque()

    def allow_request(self):
        current_time = time.time()

        # Remove expired requests
        while self.requests and self.requests[0] <= current_time - self.window:
            self.requests.popleft()

        if len(self.requests) < self.max_requests:
            self.requests.append(current_time)
            return True
        return False


# Example usage:
limiter = RateLimiter(max_requests=3, window_seconds=5)

for i in range(5):
    print("Request allowed?", limiter.allow_request())
    time.sleep(1)