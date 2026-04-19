# 🔗 LinkedList Data Structure

The **LinkedList** is a fundamental linear data structure that stores elements as a sequence of nodes, where each node contains data and a reference to the next (and sometimes previous) node.

Unlike arrays, linked lists do **not store elements in contiguous memory**. Instead, elements are dynamically allocated and connected through pointers, allowing flexible memory usage and efficient structural modifications.

This chapter introduces the LinkedList from first principles, explains its internal structure, operations, variations, and performance characteristics, and highlights its role in algorithmic problem-solving.

## 1️⃣ Introduction & Basics

### What is a LinkedList?

A **LinkedList** is a **linear data structure** composed of nodes, where each node contains:

-   Data (value)
-   Reference (pointer) to the next node

Key properties:

-   Maintains **insertion order**
-   Allows **duplicate elements**
-   Uses **non-contiguous memory**
-   Grows dynamically without resizing
-   Supports efficient insertion and deletion

Unlike arrays, linked lists do not support direct indexing.

---

### Node Structure

Each element in a linked list is stored as a node:

\[data \| next\]

For doubly linked lists:

\[prev \| data \| next\]

The list is accessed through a reference called the **head**.

---

### Why LinkedList?

Linked lists exist to overcome limitations of arrays:

-   Arrays require contiguous memory
-   Insertions/deletions are expensive (shifting required)
-   Fixed-size allocation (in static arrays)

Linked lists provide:

👉 Dynamic memory usage and structural flexibility.

## 2️⃣ Types of Linked Lists

Linked lists can be classified based on node connections.

### Singly Linked List

-   Each node points to the next node
-   Traversal is one-directional

---

### Doubly Linked List

-   Each node has:
    -   Previous pointer
    -   Next pointer
-   Supports bidirectional traversal

---

### Circular Linked List

-   Last node points back to the head
-   No null termination

---

### Circular Doubly Linked List

-   Combines circular structure with bidirectional links

## 3️⃣ Basic Operations

Linked lists support core operations that manipulate node connections.

### Insertion

-   Insert at beginning (head)
-   Insert at end (tail)
-   Insert at a specific position

---

### Deletion

-   Delete from beginning
-   Delete from end
-   Delete by value
-   Delete by position

---

### Traversal

-   Iterate node by node from head
-   Stop when reaching null (or head again in circular lists)

---

### Search

-   Linear search only (no random access)

## 4️⃣ Internal Mechanics

Understanding how LinkedLists work internally is essential.

### Memory Model

-   Nodes are stored in **non-contiguous memory**
-   Each node contains extra pointer(s)
-   Memory allocation happens dynamically

---

### Pointer Linking

Nodes are connected using references:

-   Each node points to the next node
-   Structure is maintained through pointer updates

Insertion and deletion involve:

👉 Updating pointers, not shifting elements

---

### Structural Flexibility

-   No resizing required
-   Efficient modifications when node reference is known

Tradeoff:

👉 Flexibility comes at the cost of slower access.

## 5️⃣ Time & Space Complexity

### Time Complexity

| Operation       | LinkedList |
| --------------- | ---------- |
| Access          | O(n)       |
| Insert (head)   | O(1)       |
| Insert (tail)   | O(1)\*     |
| Insert (middle) | O(n)       |
| Delete          | O(n)       |
| Search          | O(n)       |

\* O(1) if tail reference is maintained

---

### Space Complexity

-   O(n) for storing elements
-   Additional memory per node for pointers

## 6️⃣ Strengths & Weaknesses

### Strengths

-   Efficient insertion and deletion
-   Dynamic memory allocation
-   No shifting of elements
-   Flexible structure

---

### Weaknesses

-   No random access (O(n) lookup)
-   Poor cache locality
-   Extra memory overhead for pointers
-   More complex implementation

## 7️⃣ Common Patterns

LinkedLists are heavily used in algorithmic patterns.

### Core Patterns

-   **Fast & slow pointer (tortoise-hare)**
-   **Cycle detection (Floyd’s Algorithm)**
-   **Find middle element**
-   **Reverse linked list**
-   **Merge two lists**

------------------------------------------------------------------------

### Advanced Patterns

-   Reverse in k-groups
-   Intersection detection
-   Flatten multi-level lists
-   Clone list with random pointers

## 8️⃣ Real-World Applications

LinkedLists are used in many systems:

-   Implementation of stacks and queues
-   LRU Cache (with doubly linked list)
-   Browser history navigation
-   Undo/redo systems
-   Dynamic memory management

## 9️⃣ Common Pitfalls

-   Losing node references during updates
-   Null pointer dereferencing
-   Incorrect pointer updates
-   Infinite loops in circular lists
-   Off-by-one traversal errors

## 🔟 Edge Cases

Always consider:

-   Empty list
-   Single node list
-   Deleting head or tail
-   Cyclic lists
-   Duplicate values

## 1️⃣1️⃣ When to Use LinkedList

Use LinkedList when:

-   Frequent insertions and deletions are required
-   Memory needs to grow dynamically
-   Node references are available

Avoid LinkedList when:

-   Frequent random access is needed
-   Cache performance is critical

## 1️⃣2️⃣ Implementation Note

-   LinkedLists can be implemented manually using nodes
-   Libraries provide optimized versions
-   Mastery requires understanding pointer manipulation

## 1️⃣3️⃣ Summary

The LinkedList is a **dynamic and flexible data structure** that prioritizes structural operations over direct access. It trades fast indexing for efficient modifications, making it ideal for problems involving frequent insertions, deletions, and pointer manipulation. LinkedLists are not just about storing data. They train you to think in terms of **connections, references, and structure**.

Mastery of LinkedLists enables deeper understanding of:

-   Trees and graph representations
-   Stack and queue implementations
-   Pointer-based algorithms
-   Advanced problem-solving patterns