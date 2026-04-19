# 🌳 Tree Data Structure

The **Tree** is a fundamental non-linear hierarchical data structure used to represent relationships between elements. Unlike linear structures such as arrays or lists, trees model parent-child relationships, making them ideal for representing hierarchies, recursive structures, and search spaces.

Trees form the backbone of many advanced data structures and algorithms, including:

- Databases (B-Trees, B+ Trees)
- File systems
- Compilers (syntax trees)
- Networking (routing trees)
- AI/ML (decision trees)

This chapter introduces trees from first principles, explores their structure and behavior, and builds toward advanced variations and problem-solving patterns.

# 1️⃣ Introduction & Basics

## What is a Tree?

A Tree is a collection of nodes connected by edges, satisfying:

- One node is designated as the root
- Every node (except root) has exactly one parent
- Nodes may have zero or more children
- There are no cycles

### 👉 A tree with $n$ nodes always has $(n - 1)$ edges

---

### Tree as an Abstract Data Type (ADT)

A Tree is an Abstract Data Type (ADT) that defines:

- Hierarchical relationships
- Traversal mechanisms
- Structural operations

It does not define implementation details (array, pointers, etc.)

---

### Key Characteristics

- Hierarchical structure
- Recursive nature
- Non-linear organization
- Efficient representation of relationships

## 2️⃣ Tree Terminology

Understanding terminology is critical.

- **Node** — Basic unit containing data
- **Edge** — Connection between nodes
- **Root** — Topmost node
- **Parent** — Immediate predecessor
- **Child** — Immediate successor
- **Leaf** (External Node) — Node with no children
- **Internal Node** — Node with at least one child
- **Siblings** — Nodes with same parent
- **Subtree** — Tree formed by a node and its descendants
- **Degree** — Number of children of a node
- **Depth** — Distance from root
- **Height** — Longest path to a leaf
- **Level** — Depth + 1
- **Ancestor / Descendant** — Hierarchical relationship

## 3️⃣ Types of Trees

- General Tree (N-ary Tree)
- Binary Tree (≤ 2 children)
- Binary Search Tree (BST)
- Heap (Min/Max)
- Trie (Prefix Tree)

## 4️⃣ Tree Traversals

Traversal = visiting all nodes systematically

### Depth-First Search (DFS)
```
Inorder (LNR) → Left, Node, Right
Preorder (NLR) → Node, Left, Right
Postorder (LRN) → Left, Right, Node
```

### Breadth-First Search (BFS)

```
Level Order Traversal
Advanced Traversals
Morris Traversal (O(1) space)
Iterative traversals (stack-based)
Zigzag traversal
Vertical traversal
```

## 5️⃣ Basic Operations

- Insertion (Depends on tree type)
    - BST → ordered insertion
    - Heap → maintain heap property

- Deletion
    - Leaf node
    - Node with one child
    - Node with two children

- Searching
    - DFS / BFS
    - BST → $O(log n)$ average

- Traversal
    - Recursive
    - Iterative (stack/queue)

## 6️⃣ Structural Properties
- Height = Max depth of tree
- Number of Nodes:
    - Max nodes at level l = 2^l
    - Max nodes in tree of height h = 2^(h+1) - 1
- Balanced vs Unbalanced
    - Balanced → efficient operations
    - Unbalanced → degrades to O(n)

## 7️⃣ Time & Space Complexity

### Time Complexity
| Tree Type | Operation | Average | Worst |
| :--- | :--- | :--- | :--- |
| **Binary Tree** | Search / Insert / Delete | $O(n)$ | $O(n)$ |
| **BST** | Search / Insert / Delete | $O(\log n)$ | $O(n)$ |
| **Balanced Tree** | Search / Insert / Delete | $O(\log n)$ | $O(\log n)$ |
| **All Trees** | Traversal (DFS/BFS) | $O(n)$ | $O(n)$ |

### Space Complexity
| Case | Complexity | Context |
| :--- | :--- | :--- |
| **Recursive Stack** | $O(h)$ | Proportional to the height of the tree. |
| **Worst Case** | $O(n)$ | Occurs in skewed (degenerate) trees. |

## 8️⃣ Implementation Notes

### Trees can be implemented using:
- Classes (Node-based)
- Arrays (heap-style)
- Recursion is natural but iterative is important
- Always understand invariants (BST property, heap property)

## 9️⃣ Summary

The Tree data structure is a core abstraction for hierarchical relationships and recursive computation. It extends beyond simple storage into:

- Efficient searching (BST)
- Priority management (Heap)
- Range queries (Segment Tree)
- String processing (Trie)

Mastery of trees unlocks deeper understanding of:

- Graphs
- Dynamic Programming
- Divide & Conquer
- Advanced algorithms

Trees are not just a topic, they are a foundation for thinking recursively and structurally in computer science.