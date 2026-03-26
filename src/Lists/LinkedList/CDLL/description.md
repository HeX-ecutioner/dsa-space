# Circular Doubly Linked List (CDLL)

## 1. Introduction

A **Circular Doubly Linked List (CDLL)** is a variation of a doubly linked list where:

* Each node has **data, prev, and next pointers**
* The last node connects back to the first node
* The first node connects back to the last node

This forms a **closed circular structure**.

## 2. Structure of a Node

```
Node:
    data
    prev -> previous node
    next -> next node
```

Example:

```
10 <-> 20 <-> 30 (circular)
```

(30.next → 10 and 10.prev → 30)

## 3. Key Components

* **Head** → First node
* **Tail** → Last node
* **Size** → Number of elements

## 4. How It Works

* No node points to null
* Traversal wraps around automatically
* Can start traversal from any node

## 5. Operations

### 5.1 Insertion

#### (a) At Beginning

* Insert before head
* Update head and circular links

#### (b) At End

* Insert after tail
* Maintain circular connection

#### (c) At Position

* Traverse to position
* Adjust both prev and next pointers

---

### 5.2 Deletion

#### (a) From Beginning

* Move head forward
* Maintain circular links

#### (b) From End

* Move tail backward
* Maintain circular links

#### (c) By Value

* Locate node
* Reconnect neighbors

---

### 5.3 Search

* Traverse up to size times
* Compare values

---

### 5.4 Traversal

* Forward traversal using next
* Backward traversal using prev
* Must stop after full cycle

---

### 5.5 Reverse

* Swap prev and next for each node
* Swap head and tail

---

### 5.6 Find Middle

* Use fast/slow pointer with circular stopping condition

## 6. Time & Space Complexity

| Operation             | Time Complexity | Space Complexity |
| --------------------- | --------------- | ---------------- |
| Insert at Beginning   | O(1)            | O(1)             |
| Insert at End         | O(1)            | O(1)             |
| Insert at Position    | O(n)            | O(1)             |
| Delete from Beginning | O(1)            | O(1)             |
| Delete from End       | O(1)            | O(1)             |
| Delete by Value       | O(n)            | O(1)             |
| Search                | O(n)            | O(1)             |
| Traversal             | O(n)            | O(1)             |
| Reverse               | O(n)            | O(1)             |
| Find Middle           | O(n)            | O(1)             |

## 7. Advantages

* No null pointers (fully connected structure)
* Efficient traversal from any node
* Useful for cyclic processes

## 8. Disadvantages

* More complex logic due to circular nature
* Risk of infinite loops if not handled carefully
* Extra memory for prev pointer
## 9. Practical Applications

* Round-robin scheduling
* Multiplayer turn-based systems
* Music playlist looping
* Circular buffers
* Task scheduling systems

## 10. Summary

A Circular Doubly Linked List combines the benefits of doubly linked lists and circular structures, making it powerful for cyclic and continuous data processing scenarios.