# Balanced Binary Tree

## Overview
A Balanced Binary Tree (also known as a height-balanced tree) is a binary tree in which the left and right subtrees of **every node** differ in height by no more than 1.

## Why it matters
Maintaining balance is critical for performance. In a perfectly balanced tree, the height is strictly logarithmic `O(log N)`. If a tree becomes unbalanced, it can degrade into a linked list, dropping performance to `O(N)`.

## Properties
* `|Height(Left) - Height(Right)| <= 1` for all nodes.