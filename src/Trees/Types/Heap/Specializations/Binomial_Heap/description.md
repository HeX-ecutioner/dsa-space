# Binomial Heap

## Overview
A Binomial Heap is a priority queue data structure that acts as a collection of **Binomial Trees**. 

## Why does it exist?
Standard Binary Heaps (Min-Heap/Max-Heap) are great at `push` and `pop` in $O(\log N)$. However, if you want to **merge two entire heaps together**, it takes $O(N)$ time.
A Binomial Heap can merge two separate priority queues together in strictly **$O(\log N)$ time**.

## Properties
* A Binomial Tree of order $K$ has exactly $2^K$ nodes.
* A Binomial Heap uses binary arithmetic logic. If a heap has 13 elements (1101 in binary), it consists of exactly three Binomial Trees: Order 3 (8 nodes), Order 2 (4 nodes), and Order 0 (1 node).