"""
Problem: Intersection of Two Linked Lists
Statement: Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If they don't intersect, return null.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    # Time Complexity: O(m + n) - Worst case traverses both lists.
    # Space Complexity: O(1) - Elegant pointer swapping technique.
    
    if not headA or not headB:
        return None
        
    pointerA = headA
    pointerB = headB
    
    # If they are different lengths, swapping them at the ends equalizes the distance traversed
    while pointerA != pointerB:
        pointerA = pointerA.next if pointerA else headB
        pointerB = pointerB.next if pointerB else headA
        
    return pointerA

# Example usage
if __name__ == "__main__":
    intersect = ListNode(8)
    intersect.next = ListNode(4)
    
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = intersect
    
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = intersect
    
    res = getIntersectionNode(headA, headB)
    print("Intersection at:", res.val if res else "None") # Expected: 8