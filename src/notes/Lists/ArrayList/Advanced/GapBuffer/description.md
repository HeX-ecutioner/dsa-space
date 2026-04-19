# 📝 Gap Buffer

## Overview
A Gap Buffer is a specialized dynamic array primarily used in **text editors** (like VS Code or Microsoft Word). It solves the problem of $O(N)$ insertions and deletions in the middle of a standard array.

## How It Works
It maintains a "gap" (a sequence of empty slots) at the exact position of the user's cursor. 
* When the user types, characters are dropped into the gap in $O(1)$ time.
* When the user moves the cursor, the gap is shifted around the array to match the cursor's new location.

## Trade-offs
Excellent for localized edits (typing at a cursor), but moving the cursor long distances across the document requires shifting elements, which takes $O(N)$ time.