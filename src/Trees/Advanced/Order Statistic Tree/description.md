# Order Statistic Tree

## Overview
An Order Statistic Tree is an augmented Binary Search Tree (usually a Red-Black Tree) that supports finding the **$K$-th smallest element** in the tree in $O(\log N)$ time.

## The Augmentation
Every node stores an extra variable: `size`. This represents the total number of nodes in its subtree (including itself).

## How it finds the K-th element
If you want the $K$-th element, you look at the `size` of the left child.
* If `Left.size == K - 1`: The current node is the answer!
* If `Left.size >= K`: The answer is hidden in the left subtree. Search left.
* If `Left.size < K - 1`: The answer is in the right subtree. Search right, but you are now looking for the $(K - \text{Left.size} - 1)$-th element!