# Suffix Tree

## Overview
A Suffix Tree is a highly compressed Trie that contains all the **suffixes** of a given string. It is the ultimate data structure for ultra-fast string and pattern matching.

## The Power
If you have a massive text (like the entire human genome, length $N$), and you want to find a specific gene pattern (length $M$).
* Standard search takes $O(N \times M)$.
* If you build a Suffix Tree of the genome (which takes $O(N)$ time using Ukkonen's Algorithm), searching for *any* pattern takes strict **$O(M)$ time**. The length of the genome $N$ no longer matters!

## Compression
Instead of storing one character per node (like a standard Trie), edges in a Suffix Tree can store entire substrings to save space.