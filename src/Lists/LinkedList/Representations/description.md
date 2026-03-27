# Linked List Representation

## Logical Representation

A linked list is a linear data structure where elements are stored as a sequence of nodes, and each node contains data along with a reference to the next node in the sequence. Unlike arrays, elements are not stored in contiguous memory, but are connected through pointers. Linked lists maintain insertion order and allow efficient insertion and deletion operations.

## Physical Representation

Linked lists can be implemented in multiple forms based on node connectivity:

### Singly Linked List:
- Each node contains data and a reference to the next node.
- Traversal is unidirectional (forward only).
- Memory usage is minimal compared to other variants.

### Doubly Linked List:
- Each node contains data, a reference to the next node, and a reference to the previous node.
- Allows bidirectional traversal.
- Requires extra memory for the additional pointer.

### Circular Linked List:
- The last node points back to the first node instead of null.
- Forms a loop, enabling continuous traversal.

### Circular Doubly Linked List:
- Combines bidirectional traversal with a circular structure.
- Last node connects to the first, and vice versa.

## Head and Tail Pointers

Linked lists are typically accessed using special pointers:

- Head Pointer: Points to the first node in the list.
- Tail Pointer (optional): Points to the last node for efficient insertion at the end.
- Their movement is as follows:
    - Insertion at Beginning: Head pointer updates to the new node.
    - Insertion at End: Tail pointer updates to the new node (if maintained).
    - Deletion at Beginning: Head pointer moves to the next node.
    - Deletion at End: Tail pointer moves to the previous node (requires traversal in singly list).

## Diagrams and Traces

LinkedList Operations Example

```
Initial List:

null  

Insert 1 at Beginning:

1 -> null  

Insert 2 at End:

1 -> 2 -> null  

Insert 3 at Beginning:

3 -> 1 -> 2 -> null  

Delete from Beginning:

1 -> 2 -> null  // 3 is removed
```

## Pointer Movement

```
After inserting 1: Head -> 1
After inserting 2: Tail -> 2
After inserting 3 at beginning: Head -> 3
After deletion: Head -> 1
```