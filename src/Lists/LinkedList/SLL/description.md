# Singly Linked List (SLL)

## 1. Introduction

A **Singly Linked List (SLL)** is a linear data structure where elements are stored in nodes. Each node contains:

* **Data** (value)
* **Pointer (next)** to the next node in the list

Unlike arrays, linked lists do not use contiguous memory. Elements are connected via pointers.

## 2. Structure of a Node

```
Node:
    data
    next -> reference to next node
```

Example:

```
10 -> 20 -> 30 -> null
```

## 3. Key Components

* **Head** → Points to first node
* **Tail** → Points to last node (optional but useful)
* **Size** → Tracks number of elements (optional)

## 4. How It Works

* The list starts from the **head**
* Each node points to the **next node**
* The last node points to **null**

Traversal is always sequential (no direct indexing)

## 5. Operations

### 5.1 Insertion

#### (a) At Beginning

* Create new node
* Point it to current head
* Update head

#### (b) At End

* Traverse to last node OR use tail
* Update last node’s next

#### (c) At Position

* Traverse to position - 1
* Adjust pointers

---

### 5.2 Deletion

#### (a) From Beginning

* Move head to next node

#### (b) From End

* Traverse to second last node
* Set its next to null

#### (c) By Value

* Search for node
* Update previous node’s next

---

### 5.3 Search

* Traverse list
* Compare each node

---

### 5.4 Traversal (Display)

* Visit each node from head to null

---

### 5.5 Reverse

* Reverse pointers using three variables:

  * prev
  * current
  * next

---

### 5.6 Find Middle

* Use **slow and fast pointer** technique

## 6. Time & Space Complexity

| Operation                 | Time Complexity | Space Complexity |
| ------------------------- | --------------- | ---------------- |
| Insert at Beginning       | O(1)            | O(1)             |
| Insert at End (with tail) | O(1)            | O(1)             |
| Insert at Position        | O(n)            | O(1)             |
| Delete from Beginning     | O(1)            | O(1)             |
| Delete from End           | O(n)            | O(1)             |
| Delete by Value           | O(n)            | O(1)             |
| Search                    | O(n)            | O(1)             |
| Traversal                 | O(n)            | O(1)             |
| Reverse                   | O(n)            | O(1)             |
| Find Middle               | O(n)            | O(1)             |

## 7. Advantages

* Dynamic size
* Efficient insertion/deletion
* No memory wastage (no unused capacity like arrays)

## 8. Disadvantages

* No random access (O(n))
* Extra memory for pointer
* Not cache-friendly

## 9. Practical Applications

* Implementing stacks and queues
* Memory management (free lists)
* Graph adjacency lists
* Undo/redo systems
* Hash table chaining
* Music playlist / navigation systems


## 10. Summary

A Singly Linked List is a flexible data structure ideal for dynamic data where frequent insertions and deletions are required, but direct access is not needed.