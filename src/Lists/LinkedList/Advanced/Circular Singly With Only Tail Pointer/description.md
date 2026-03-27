# CIRCULAR SINGLY LINKED LIST (TAIL POINTER ONLY)

A Circular Singly Linked List is a variation of a singly linked list where:

* The last node does NOT point to null
* Instead, it points back to the first node (head)

## Key Idea:
The list forms a cycle:
tail.next → head

## Special Design: ONLY Tail Pointer

Instead of storing both head and tail:

* We store only the tail pointer

From tail, we can access head:
head = tail.next

## Why use only tail?

* Saves one pointer (head not stored explicitly)
* Efficient insertion at:

  * Beginning → O(1)
  * End → O(1)

## Operations

### Insertion:

* At beginning → insert after tail, update head
* At end → insert after tail, move tail forward

### Deletion:

* From beginning → remove head (tail.next)
* From end → requires traversal (O(n))
* By value → requires traversal

### Traversal:

* Start from head (tail.next)
* Stop when we reach head again

## Edge Cases

* Empty list (tail = None)
* Single node (tail.next = tail)
* Deleting the only node
* Circular traversal stopping condition

## Complexity

| Operation      | Time |
| -------------- | ---- |
| Insert (begin) | O(1) |
| Insert (end)   | O(1) |
| Delete (begin) | O(1) |
| Delete (end)   | O(n) |
| Search         | O(n) |

## Summary

Using only a tail pointer is an elegant optimization that:

* Keeps the structure minimal
* Maintains efficient operations
* Forces deeper understanding of circular references