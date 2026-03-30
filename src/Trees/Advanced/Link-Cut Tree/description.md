# Link-Cut Tree

## Overview
The Link-Cut tree is one of the most complex dynamic data structures. It represents a **forest** (a collection of trees) and allows you to dynamically `link` two trees together or `cut` a tree into two smaller trees in $O(\log N)$ time.

## How it works
It uses a combination of Heavy-Light Decomposition concepts and **Splay Trees**. 
Every represented tree is partitioned into paths. Each path is stored in a Splay Tree ordered by depth. 
* To do anything, you perform an `access(v)` operation, which restructures the internal Splay trees so that node `v` and the root of its represented tree form a single, contiguous Splay Tree path.

## Use Cases
* Dynamic Connectivity problems (e.g., "Is node A connected to node B right now, considering I just deleted the edge between C and D?").