"""
Problem: Merge Two Sorted Lists
Statement: You are given the heads of two sorted linked lists. Merge the two lists into one sorted list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # Time Complexity: O(n + m) - Where n and m are lengths of list1 and list2.
    # Space Complexity: O(1) - Only pointers are adjusted.
    
    dummy = ListNode(-1)
    curr = dummy
    
    while list1 and list2:
        # Compare values and attach the smaller one
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
        
    # Attach any remaining elements from either list
    curr.next = list1 if list1 else list2
    
    return dummy.next

# Example usage
if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    
    merged = mergeTwoLists(l1, l2)
    res = []
    while merged:
        res.append(merged.val)
        merged = merged.next
    print("Merged List:", res) # Expected: [1, 1, 2, 3, 4, 4]