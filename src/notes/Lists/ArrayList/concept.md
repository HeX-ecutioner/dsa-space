# 📦 ArrayList Data Structure

The **ArrayList** is a dynamic linear data structure that stores elements in a contiguous block of memory and automatically resizes as elements are added or removed.

Unlike static arrays, ArrayLists provide **flexible sizing** while maintaining the advantages of fast access and cache efficiency.

This chapter introduces the ArrayList from first principles, explains its internal structure, operations, variations, and performance characteristics, and highlights its role in algorithmic problem-solving.

## 1️⃣ Introduction & Basics

### What is an ArrayList?

An **ArrayList** is a **resizable array-based data structure** that allows dynamic addition and removal of elements.

Key properties:

* Maintains **insertion order**
* Allows **duplicate elements**
* Uses **contiguous memory**
* Supports **random access (indexing)**
* Automatically resizes when capacity is exceeded

---

### Internal Structure

ArrayList is backed by a **dynamic array**:

[data₀, data₁, data₂, ...]

* Elements are stored in contiguous memory
* A **capacity** defines total allocated space
* A **size** tracks current number of elements

---

### Why ArrayList?

ArrayLists solve limitations of static arrays:

* Fixed size restriction
* Manual resizing complexity

They provide:

👉 Dynamic resizing with fast access.

## 2️⃣ Types of Array-Based Lists

### Static Array

* Fixed size
* Cannot grow dynamically

---

### Dynamic Array (ArrayList)

* Automatically resizes
* Most commonly used

---

### Vector (Language-specific)

* Thread-safe dynamic array (e.g., Java Vector)

## 3️⃣ Basic Operations

### Insertion

* Insert at end (append)
* Insert at beginning
* Insert at specific index

---

### Deletion

* Delete from end
* Delete from beginning
* Delete by index
* Delete by value

---

### Access

* Direct access using index (O(1))

---

### Traversal

* Iterate using loops or iterators

---

### Search

* Linear search (unsorted)
* Binary search (if sorted)

## 4️⃣ Internal Mechanics

### Memory Model

* Stored in **contiguous memory blocks**
* Uses an underlying array

---

### Resizing Strategy

When capacity is full:

* A new array (usually **2× capacity**) is created
* Elements are copied
* Old array is discarded

---

### Amortized Cost

* Resizing is expensive (O(n))
* But happens infrequently

👉 Average insertion remains **O(1) amortized**

---

### Cache Efficiency

* Better cache locality compared to linked lists
* Faster iteration due to contiguous storage

## 5️⃣ Time & Space Complexity

### Time Complexity

| Operation       | ArrayList |
| --------------- | --------- |
| Access          | O(1)      |
| Insert (end)    | O(1)*     |
| Insert (middle) | O(n)      |
| Delete (end)    | O(1)      |
| Delete (middle) | O(n)      |
| Search          | O(n)      |

* Amortized O(1)

---

### Space Complexity

* O(n) for storing elements
* Extra unused capacity due to resizing

## 6️⃣ Strengths & Weaknesses

### Strengths

* Fast random access (O(1))
* Cache-friendly (better performance)
* Simple implementation
* Dynamic resizing

---

### Weaknesses

* Expensive insertions/deletions in middle (O(n))
* Resizing overhead (copying elements)
* Possible unused memory due to extra capacity

## 7️⃣ Common Patterns

### Core Patterns

* **Two-pointer technique**
* **Sliding window**
* **Prefix sums**
* **Binary search on arrays**

---

### Advanced Patterns

* Dynamic resizing optimization
* In-place array manipulation
* Partitioning (quick sort style)
* Kadane’s algorithm (maximum subarray)

## 8️⃣ Real-World Applications

ArrayLists are widely used in:

* Dynamic collections in programming languages
* Database query results
* Game development (entity lists)
* Data processing pipelines
* Buffer management

## 9️⃣ Common Pitfalls

* Ignoring resizing cost
* Frequent insertions at beginning
* Index out-of-bounds errors
* Inefficient shifting operations

## 🔟 Edge Cases

Always consider:

* Empty list
* Single element
* Full capacity triggering resize
* Large data causing memory overhead

## 1️⃣1️⃣ When to Use ArrayList

Use ArrayList when:

* Frequent random access is required
* Iteration performance matters
* Insertions mostly happen at the end

Avoid ArrayList when:

* Frequent insertions/deletions in middle
* Memory overhead must be minimized strictly

## 1️⃣2️⃣ Implementation Note

* Backed by dynamic arrays
* Language libraries provide optimized versions
* Understanding resizing is key to mastery

## 1️⃣3️⃣ Summary

The ArrayList is a **high-performance dynamic data structure** that combines the speed of arrays with the flexibility of dynamic resizing. It is ideal for applications requiring fast access, iteration, and moderate structural modifications.

Mastery of ArrayLists enables deeper understanding of:

* Memory management and resizing strategies
* Algorithm optimization using arrays
* Efficient data storage and access patterns
* Core problem-solving techniques in competitive programming
