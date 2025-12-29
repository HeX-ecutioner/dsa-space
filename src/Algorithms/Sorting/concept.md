# 🔀 Sorting Algorithms

**Sorting** is one of the most fundamental topics in data structures and algorithms.
It focuses on rearranging data into a specific order (usually ascending or descending)
to make it easier, faster, and more efficient to process.

Sorting is not just a standalone problem — it is a **building block** for searching,
optimization, data analysis, and many advanced algorithmic techniques.

This chapter introduces the concept of sorting, explains why it matters, discusses
classification and complexity, and compares the most common sorting algorithms at a
conceptual level.

---

## 1️⃣ Introduction & Basics

### What is Sorting?

Sorting is the process of **rearranging elements of a collection** so that they follow
a defined order, such as:

* Ascending order (smallest → largest)
* Descending order (largest → smallest)
* Lexicographical order (strings)
* Custom order based on a key or comparator

The data being sorted can be numbers, strings, objects, or records.

### Why Sorting is Important

Sorting improves efficiency and clarity:

* Enables faster searching (e.g., binary search)
* Simplifies duplicate detection
* Helps with grouping and aggregation
* Makes data easier to analyze and visualize
* Serves as a preprocessing step for many algorithms

Many real-world systems rely heavily on efficient sorting.

### Real-World Analogies

Sorting appears naturally in daily life:

* Arranging books alphabetically
* Ranking students by score
* Sorting files by date or size
* Organizing contacts by name

These analogies mirror how computers organize data internally.

---

## 2️⃣ Classification of Sorting Algorithms

Sorting algorithms can be classified based on several criteria.

### Based on Time Complexity

* **Quadratic-time sorts (O(n²))**

  * Bubble Sort
  * Selection Sort
  * Insertion Sort

* **Efficient sorts (O(n log n))**

  * Merge Sort
  * Quick Sort
  * Heap Sort

* **Linear-time sorts (O(n))** (under specific constraints)

  * Counting Sort
  * Radix Sort
  * Bucket Sort

---

### Based on Stability

* **Stable Sorts**

  * Preserve the relative order of equal elements
  * Important when sorting records with multiple keys

* **Unstable Sorts**

  * May change the order of equal elements

---

### Based on Memory Usage

* **In-place Sorting**

  * Requires constant or minimal extra memory
  * Example: Quick Sort, Insertion Sort

* **Out-of-place Sorting**

  * Requires additional memory proportional to input size
  * Example: Merge Sort

---

## 3️⃣ Comparison-Based vs Non-Comparison Sorting

### Comparison-Based Sorting

These algorithms sort elements by **comparing pairs of values**.

* Lower bound: **O(n log n)** comparisons
* Works for any comparable data

Examples:

* Merge Sort
* Quick Sort
* Heap Sort
* Bubble / Insertion / Selection Sort

---

### Non-Comparison Sorting

These algorithms do **not compare elements directly**.
Instead, they use properties of the data (digits, range, buckets).

* Can achieve **O(n)** time
* Require constraints on input

Examples:

* Counting Sort
* Radix Sort
* Bucket Sort

---

## 4️⃣ Core Sorting Algorithms (Conceptual Overview)

### Simple Sorting Algorithms

* **Bubble Sort**

  * Repeatedly swaps adjacent elements
  * Simple but inefficient

* **Selection Sort**

  * Selects the minimum element and places it correctly
  * Predictable but slow

* **Insertion Sort**

  * Builds the sorted array incrementally
  * Efficient for small or nearly sorted data

---

### Efficient Sorting Algorithms

* **Merge Sort**

  * Divide-and-conquer strategy
  * Stable and predictable
  * Requires extra memory

* **Quick Sort**

  * Partition-based divide-and-conquer
  * Very fast in practice
  * Worst case O(n²) if poorly implemented

* **Heap Sort**

  * Uses a binary heap
  * Guaranteed O(n log n)
  * Not stable

---

### Linear-Time Sorting Algorithms

* **Counting Sort**

  * Counts occurrences of values
  * Works for small integer ranges

* **Radix Sort**

  * Sorts digit by digit
  * Depends on stable sub-sorting

* **Bucket Sort**

  * Distributes elements into buckets
  * Performance depends on distribution

---

## 5️⃣ Time & Space Complexity

### Time Complexity (General)

* Best case: already sorted or favorable input
* Average case: expected performance
* Worst case: most unfavorable input

Understanding all three is critical when choosing a sorting algorithm.

---

### Space Complexity

* In-place sorts use **O(1)** or **O(log n)** extra space
* Out-of-place sorts use **O(n)** extra space

Memory constraints often influence algorithm choice as much as speed.

---

## 6️⃣ Sorting vs Other Techniques

### Sorting vs Searching

* Sorting rearranges data
* Searching locates data

Sorting often enables faster searching later.

---

### Sorting vs Hashing

* Sorting maintains order
* Hashing focuses on fast access

Each serves different purposes depending on requirements.

---

## 7️⃣ When to Use Which Sorting Algorithm

Guidelines for selection:

* Small input size → Insertion Sort
* Large datasets → Merge Sort / Quick Sort
* Memory constrained → Heap Sort
* Stable sorting needed → Merge Sort
* Integer range known → Counting / Radix Sort

There is no universally best sorting algorithm.

---

## 8️⃣ Advantages & Limitations of Sorting

### Advantages

* Improves efficiency of many algorithms
* Makes data easier to analyze
* Essential for searching and grouping
* Widely supported in libraries

### Limitations

* Sorting can be expensive for large data
* Some algorithms require extra memory
* Poor algorithm choice leads to performance issues

---

## 9️⃣ Summary

Sorting algorithms form the backbone of efficient data processing.
Understanding their behavior, complexity, and trade-offs is essential
for writing high-performance and scalable software.

Mastery of sorting enables:

* Faster searching
* Cleaner logic
* Better algorithm design
* Strong interview performance

This folder builds from conceptual understanding to practical
problem-solving using sorting algorithms.
