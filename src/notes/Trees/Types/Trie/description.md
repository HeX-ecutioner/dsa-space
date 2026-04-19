# Trie (Prefix Tree)

## Overview
A Trie is an N-ary tree specialized for storing and searching strings. Rather than storing an entire string in a single node, strings are broken down into characters. Each path down the tree represents a word.

## Structure
* The root represents an empty string.
* Every node contains an array (or Hash Map) of pointers to its possible children (e.g., 26 pointers for the English alphabet).
* Nodes contain a boolean flag `is_end_of_word` to mark where a valid dictionary word finishes.

## Why use it over a Hash Set?
If you have a Hash Set of words, checking if any word *starts with* a specific prefix takes `O(N * M)`. A Trie can check a prefix in strict `O(M)` time, where `M` is the length of the prefix. 

## Applications
* Search Engine Autocomplete
* Spell Checkers
* IP Routing (Longest Prefix Match)