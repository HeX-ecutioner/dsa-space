"""
Problem: Find Median from Data Stream (LeetCode 295)
Statement: Maintain two heaps (a Max-Heap for the lower half, a Min-Heap for the upper half) to find the median of a continuous stream in O(1) time.
"""
import heapq

class MedianFinder:
    # Time Complexity: O(log N) for addNum, O(1) for findMedian.
    # Space Complexity: O(N) to hold the stream.

    def __init__(self):
        # Python's heapq is a Min-Heap by default. 
        # We simulate a Max-Heap by pushing negative values.
        self.small_half = [] # Max-Heap (stores the smaller half of numbers)
        self.large_half = [] # Min-Heap (stores the larger half of numbers)

    def addNum(self, num: int) -> None:
        # 1. Always push to the small (Max-Heap) first
        heapq.heappush(self.small_half, -num)
        
        # 2. Ensure every element in small_half is <= every element in large_half
        if self.small_half and self.large_half and (-self.small_half[0] > self.large_half[0]):
            val = -heapq.heappop(self.small_half)
            heapq.heappush(self.large_half, val)
            
        # 3. Balance the sizes (small_half can have at most 1 more element than large_half)
        if len(self.small_half) > len(self.large_half) + 1:
            val = -heapq.heappop(self.small_half)
            heapq.heappush(self.large_half, val)
        elif len(self.large_half) > len(self.small_half):
            val = heapq.heappop(self.large_half)
            heapq.heappush(self.small_half, -val)

    def findMedian(self) -> float:
        # If lengths are unequal, small_half has the extra element (the exact middle)
        if len(self.small_half) > len(self.large_half):
            return float(-self.small_half[0])
            
        # If lengths are equal, the median is the average of the two tops
        return (-self.small_half[0] + self.large_half[0]) / 2.0

# Example usage
if __name__ == "__main__":
    stream = MedianFinder()
    
    stream.addNum(1)
    stream.addNum(2)
    print("Median of [1, 2]:", stream.findMedian()) # Expected: 1.5
    
    stream.addNum(3)
    print("Median of [1, 2, 3]:", stream.findMedian()) # Expected: 2.0