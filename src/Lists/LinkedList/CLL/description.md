# Circular Linked List (CLL)

## 1. Introduction

A **Circular Linked List (CLL)** is a variation of a singly linked list where:

* Each node contains **data and a next pointer**
* The last node points back to the head node instead of null

This creates a **loop (circular structure)**.

## 2. Structure of a Node

```
Node:
    data
    next -> next node
```

Example:

```
10 -> 20 -> 30 -> (head)
```

(30.next → 10)

## 3. Key Components

* **Head** → First node
* **Tail** → Last node
* **Size** → Number of elements

## 4. How It Works

* No node points to null
* The list forms a continuous loop
* Traversal must be controlled to avoid infinite cycles

## 5. Operations

### 5.1 Insertion

#### (a) At Beginning

* Insert before head
* Update tail link to new head

#### (b) At End

* Insert after tail
* Maintain circular connection

#### (c) At Position

* Traverse to position
* Adjust next pointers

---

### 5.2 Deletion

#### (a) From Beginning

* Move head forward
* Update tail connection

#### (b) From End

* Traverse to second last node
* Update tail and circular link

#### (c) By Value

* Locate node
* Reconnect surrounding nodes

---

### 5.3 Search

* Traverse up to size times
* Compare each node

### 5.4 Traversal

* Start from head
* Stop after full cycle (size nodes)

### 5.5 Reverse

* Reverse links while maintaining circular structure
* Swap head and tail

### 5.6 Find Middle

* Use fast/slow pointer with circular stopping condition

## 6. Time & Space Complexity

| Operation             | Time Complexity | Space Complexity |
| --------------------- | --------------- | ---------------- |
| Insert at Beginning   | O(1)            | O(1)             |
| Insert at End         | O(1)            | O(1)             |
| Insert at Position    | O(n)            | O(1)             |
| Delete from Beginning | O(1)            | O(1)             |
| Delete from End       | O(n)            | O(1)             |
| Delete by Value       | O(n)            | O(1)             |
| Search                | O(n)            | O(1)             |
| Traversal             | O(n)            | O(1)             |
| Reverse               | O(n)            | O(1)             |
| Find Middle           | O(n)            | O(1)             |

## 7. Advantages

* No null pointers
* Efficient circular traversal
* Useful for cyclic applications

## 8. Disadvantages

* Risk of infinite loops
* More complex traversal logic
* No direct access (O(n))

## 9. Practical Applications

* Round-robin CPU scheduling
* Multiplayer turn rotation
* Circular buffers
* Continuous task scheduling

## 10. Summary

A Circular Linked List is useful for applications requiring repeated traversal without restarting, offering efficient cyclic data handling with careful control of traversal logic.
