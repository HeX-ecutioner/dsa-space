# 🛤️ Parallel Arrays

## Overview
Parallel arrays involve using multiple standard arrays of the same length to represent a single dataset, where the $i$-th element of each array belongs to the same logical entity.

## The Vibe
Instead of `Person` objects stored in one array:
`[{name: "A", age: 10}, {name: "B", age: 20}]`

You use parallel arrays:
`names = ["A", "B"]`
`ages = [10, 20]`

## Why does this exist?
While Object-Oriented Programming made this pattern less common, it is heavily used today in **Data-Oriented Design (DOD)** and **Entity Component Systems (ECS)** in video game engines. It maximizes **CPU Cache Locality** when you only need to process one specific trait (e.g., iterating through thousands of ages without loading the names into the CPU cache).