# 🗺️ K-D Tree (K-Dimensional Tree)

## Overview
A K-D Tree is a space-partitioning data structure for organizing points in a K-Dimensional space. 

## How it works
It is a standard Binary Search Tree, but the dimension it uses to compare nodes **alternates** as you go down the tree.
* Root Level: Compare X coordinates.
* Level 1: Compare Y coordinates.
* Level 2: Compare Z coordinates (if 3D), or back to X (if 2D).

## Applications
* Nearest Neighbor Search (e.g., "Find the 5 closest restaurants to my GPS coordinates").
* Collision detection in Physics Engines / Game Dev.