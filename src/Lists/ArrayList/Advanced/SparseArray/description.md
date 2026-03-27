# 🌌 Sparse Array

## Overview
A Sparse Array is a data structure used when you need an array with a massive capacity (e.g., millions of indices), but you know that **99% of the values will be empty** or a default value (like 0).

## How It Works
Instead of actually allocating millions of continuous slots in memory, a Sparse Array uses a **Hash Map / Dictionary** under the hood. 
* The keys are the array indices.
* The values are the actual data.
* If an index isn't in the Hash Map, the structure simply returns the default value (0).

## Trade-offs
It saves massive amounts of RAM, but access time drops from a guaranteed hardware-level $O(1)$ to an average-case Hash Map $O(1)$, which carries a bit more overhead.