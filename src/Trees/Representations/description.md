# Tree Representation

## Logical Representation
A **Tree** is a non-linear, hierarchical data structure consisting of nodes connected by edges. Unlike linear structures (Stacks/Queues), a tree represents a "one-to-many" relationship. It is defined recursively: a tree consists of a **root** node and zero or more **subtrees**, each of which is also a tree.

## Physical Representation
Trees can be implemented in several ways depending on the required efficiency for access, search, or memory overhead.

### 1. Linked Representation (Most Common)
This is the standard pointer-based implementation. Each node is a discrete object in memory.

* **Binary Tree Node**: Contains a data field and two pointers (`left` and `right`).
    * `[ left_pointer | data | right_pointer ]`
* **N-ary Tree Node**: Contains a data field and a dynamic list or array of pointers to its children.
    * `[ data | children_list[] ]`



### 2. Array Representation (Sequential)
Mainly used for **Complete Binary Trees** and **Heaps**. Elements are stored in contiguous memory, and parent-child relationships are calculated using indices rather than pointers.

If a node is at **index $i$** (starting at 0):
* **Left Child**: $2i + 1$
* **Right Child**: $2i + 2$
* **Parent**: $\lfloor (i - 1) / 2 \rfloor$



### 3. Parent Array Representation
A compact representation where the array index represents the **Node ID**, and the value at that index represents its **Parent's ID**.
* **Root Node**: Usually represented by a value of `-1`.
* **Primary Use**: Disjoint Set Union (DSU) and Union-Find algorithms.

### 4. Adjacency List Representation
The tree is treated as a sparse graph. An array of lists is maintained where `list[i]` contains all neighbors (children/parent) of node `i`.
* **Use Case**: When the tree needs to be processed using general graph algorithms (like Dijkstra's or finding bridge edges).

### 5. Adjacency Matrix
A 2D $N \times N$ boolean matrix where `matrix[i][j] = 1` indicates an edge exists.
* **Status**: **Rarely used** for trees. Since a tree has only $N-1$ edges, an $N^2$ matrix is highly space-inefficient.

## Diagrams and Traces

### Array Mapping Trace
Given a Binary Heap stored in an array: `[10, 20, 30, 40, 50]`

1.  **Root**: Index 0 (Value: 10)
2.  **Children of 10**:
    * Left: $2(0) + 1 = 1$ (Value: 20)
    * Right: $2(0) + 2 = 2$ (Value: 30)
3.  **Children of 20**:
    * Left: $2(1) + 1 = 3$ (Value: 40)
    * Right: $2(1) + 2 = 4$ (Value: 50)
4.  **Parent of 50**:
    * Index: $\lfloor (4 - 1) / 2 \rfloor = 1$ (Value: 20)

### Pointer Movement (Linked)
* **Moving Down**: `current = current.left` or `current = current.right`
* **Moving Up**: Not possible in a Singly Linked Tree unless a `parent` pointer is explicitly added to the node structure.

## 📊 Representation Summary

| Feature | Linked (Pointers) | Array (Sequential) | Parent Array |
| :--- | :--- | :--- | :--- |
| **Memory Locality** | Poor (Scattered) | Excellent (Contiguous) | Good |
| **Random Access** | No | Yes (via Math) | No |
| **Growth** | Dynamic | Requires Resizing | Dynamic |
| **Overhead** | High (2-3 pointers/node) | Low (Data only) | Very Low |
| **Best For** | BSTs, General Trees | Heaps, Complete Trees | Union-Find |