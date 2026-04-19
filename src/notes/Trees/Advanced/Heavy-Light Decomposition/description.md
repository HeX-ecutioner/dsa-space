# Heavy-Light Decomposition (HLD)

## Overview
Heavy-Light Decomposition is an advanced technique used to break down a tree into a set of disjoint paths (chains). It is primarily used in competitive programming to perform **Range Queries on a path between two nodes** in $O(\log^2 N)$ time.

## How it Works
1. **Find Subtree Sizes:** Do a DFS to calculate the size of every subtree.
2. **Define Heavy/Light Edges:** For any node, the edge to its child with the *largest* subtree is a **Heavy Edge**. All other edges to children are **Light Edges**.
3. **Form Chains:** Consecutive Heavy Edges form a "Heavy Path" (or chain). 

## The Magic
By flattening these Heavy Paths into a 1D array, you can use a **Segment Tree** on them. Any path between two nodes $U$ and $V$ in the tree will cross at most $O(\log N)$ light edges, meaning you only need to query at most $O(\log N)$ heavy chains in your Segment Tree!