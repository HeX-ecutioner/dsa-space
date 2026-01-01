# 🧱 Stack Data Structure

The **Stack** is one of the most fundamental and widely used data structures in computer science.
It represents a collection of elements with a very strict access rule, making it simple, fast,
and extremely useful in both theoretical and practical applications.

Unlike arrays or lists where elements can be accessed arbitrarily, a stack restricts all
insertions and deletions to **one end only**, enforcing a disciplined access pattern.

This chapter introduces the stack data structure from first principles, explains its core
operations, analyzes its performance, and compares it with other common data structures.

---

## 1️⃣ Introduction & Basics

### What is a Stack?

A **Stack** is a **linear data structure** that follows the **Last In, First Out (LIFO)** principle.
The last element inserted into the stack is the first one to be removed.

Think of it as a vertical container where you can only interact with the topmost item.

### LIFO Principle (Last In, First Out)

* The most recently added element is accessed first
* Earlier elements must wait until all newer elements are removed

This strict order defines all stack behavior.

### Stack as an Abstract Data Type (ADT)

A stack is often described as an **Abstract Data Type (ADT)**, meaning:

* It defines **what operations are allowed**
* It does not define **how those operations are implemented**

The same stack ADT can be implemented using arrays, linked lists, or other structures.

### Real-World Analogies

Stacks appear naturally in everyday life:

* **Plates stacked on a table** → last plate placed is removed first
* **Books piled on a desk** → you remove the top book first
* **Undo history in editors** → most recent action is undone first
* **Browser navigation** → backtracking through pages

### When and Why Stacks Are Used

Stacks are used when:

* Order of processing matters
* Reversal of operations is needed
* Nested structures must be tracked
* Temporary storage with strict access rules is required

They are especially common in compilers, interpreters, and system-level software.

---

## 2️⃣ Stack Terminology

Understanding stack terminology is essential before working with stack algorithms.

* **Stack** – The entire collection of elements
* **Top** – The position where insertion and deletion occur
* **Bottom** – The base of the stack (least accessible element)
* **Element** – An individual item stored in the stack
* **Size / Capacity** – Maximum number of elements the stack can hold
* **Empty Stack** – A stack with no elements
* **Full Stack** – A stack that has reached its maximum capacity

All stack operations revolve around the **top** pointer.

---

## 3️⃣ Basic Stack Operations

A stack supports a small, fixed set of operations.

### Push (Insert)

* Adds an element to the top of the stack
* Increases the stack size by one
* Fails if the stack is already full (overflow)

### Pop (Remove)

* Removes the top element from the stack
* Decreases the stack size by one
* Fails if the stack is empty (underflow)

### Peek / Top

* Returns the top element without removing it
* Useful for inspection and condition checks

### isEmpty

* Checks whether the stack has zero elements
* Used to prevent underflow

### isFull

* Checks whether the stack has reached capacity
* Relevant mainly for array-based stacks

### Time Complexity of Operations

All basic stack operations run in **O(1)** time because:

* Only the top element is accessed
* No traversal or shifting is required

---

## 4️⃣ Time & Space Complexity

### Time Complexity

For a stack:

* Push → **O(1)**
* Pop → **O(1)**
* Peek → **O(1)**
* isEmpty / isFull → **O(1)**

This constant-time performance is one of the biggest strengths of stacks.

### Space Complexity

Space usage depends on implementation:

* **Array-based stack**

  * Fixed or dynamic size
  * Possible unused allocated memory

* **Linked-list stack**

  * Memory allocated per element
  * No wasted capacity, but extra pointer overhead

### Array vs Linked List Stack

* Array stack: faster access, simpler, but fixed-size issues
* Linked list stack: flexible size, but higher memory overhead

---

## 5️⃣ Stack vs Other Data Structures

### Stack vs Queue

* Stack → LIFO (Last In, First Out)
* Queue → FIFO (First In, First Out)

Stacks are used for reversal and backtracking, queues are used for scheduling and sequential processing.

### Stack vs Array

* Stack restricts access to one end
* Array allows random access

Stacks sacrifice flexibility for simplicity and speed.

### Stack vs Linked List

* Stack defines behavior
* Linked list defines storage structure

A stack can be implemented *using* a linked list, but they are not the same concept.

### When to Use Stack Over Others

Use a stack when:

* Order reversal is required
* Nested operations exist
* Temporary state tracking is needed
* Only recent data matters

---

## 6️⃣ Advantages & Limitations

### Advantages

* Simple and intuitive implementation
* Extremely fast operations (O(1))
* Essential for recursion and expression parsing
* Widely supported in programming languages

### Limitations

* Restricted access (only top element accessible)
* Not suitable for searching or random access
* Fixed size issues in array-based stacks

Stacks are powerful but specialized, they excel when used in the right scenarios.

---

## 7️⃣ Summary

The Stack data structure enforces a strict LIFO order that enables efficient, predictable behavior. Its simplicity, speed, and strong theoretical foundation make it indispensable in computer science.

Stacks form the backbone of:

* Function calls and recursion
* Expression evaluation
* Backtracking algorithms
* Syntax parsing and compilers

Mastering stacks is a crucial step toward understanding more advanced data structures and algorithmic patterns.