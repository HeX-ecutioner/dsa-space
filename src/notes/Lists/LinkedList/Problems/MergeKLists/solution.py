"""
Problem: Merge k Sorted Lists
Statement: You are given an array of k linked-lists, each sorted in ascending order. Merge all into one sorted linked list.
"""
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    # Time Complexity: O(N log k) - N is total nodes, priority queue holds at most k elements.
    # Space Complexity: O(k) - For the heap.
    
    # We must implement __lt__ for ListNode if we insert them directly into heapq, 
    # OR we can store a tuple (val, index, node) to avoid comparing nodes.
    
    min_heap = []
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(min_heap, (l.val, i, l))
            
    dummy = ListNode(0)
    curr = dummy
    
    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        curr.next = node
        curr = curr.next
        
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))
            
    return dummy.next

# Example usage
if __name__ == "__main__":
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    
    merged = mergeKLists([l1, l2, l3])
    res = []
    while merged:
        res.append(merged.val)
        merged = merged.next
    print("Merged K Lists:", res) # Expected: [1, 1, 2, 3, 4, 4, 5, 6]