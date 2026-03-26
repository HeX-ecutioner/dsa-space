# Doubly Linked List (DLL)

## 1. Introduction

A **Doubly Linked List (DLL)** is a linear data structure where each node contains:

* **Data**
* **Pointer to next node (next)**
* **Pointer to previous node (prev)**

This allows traversal in both directions.

## 2. Structure of a Node

```
Node:
    data
    prev -> previous node
    next -> next node
```

Example:

```
null <- 10 <-> 20 <-> 30 -> null
```

## 3. Key Components

* **Head** → First node
* **Tail** → Last node
* **Size** → Number of elements

## 4. How It Works

* Each node connects forward and backward
* Enables **bidirectional traversal**
* No random access (sequential traversal required)

## 5. Operations

### 5.1 Insertion

#### (a) At Beginning

* Create node
* Link with current head
* Update head

#### (b) At End

* Use tail pointer
* Update tail links

#### (c) At Position

* Traverse to position
* Adjust both prev and next pointers

---

### 5.2 Deletion

#### (a) From Beginning

* Move head forward
* Remove prev link

#### (b) From End

* Move tail backward
* Remove next link

#### (c) By Value

* Locate node
* Update both neighboring links

---

### 5.3 Search

* Traverse from head
* Compare values

### 5.4 Traversal

* Forward traversal using next
* Backward traversal using prev

### 5.5 Reverse

* Swap prev and next pointers for each node
* Swap head and tail

### 5.6 Find Middle

* Use **slow and fast pointer** technique

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

* Bidirectional traversal
* Easier deletion (no need to track previous node externally)
* Efficient operations at both ends

## 8. Disadvantages

* Extra memory for prev pointer
* More complex pointer handling
* Slightly slower due to additional updates

## 9. Practical Applications

* Browser navigation (back/forward)
* Undo/redo functionality
* Navigation systems
* Music/video playlist navigation
* Implementing deques

## 10. Summary

A Doubly Linked List enhances a singly linked list by allowing traversal in both directions, making it more flexible at the cost of extra memory and complexity.