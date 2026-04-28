# 🧹 Sweep Line

The **Sweep Line** technique (also known as Line Sweep) is a conceptual method used to solve geometric and interval-based problems efficiently.

Imagine a vertical or horizontal line sweeping across a plane (or an array of intervals) from left to right. As the line moves, we only care about the "events" where the line encounters the start or end of an object. 

---

## 1️⃣ What is the Sweep Line Technique?

Instead of comparing every interval/object with every other interval (which takes O(N²)), we:
1. Break down intervals/shapes into individual **events** (e.g., "Start at x1", "End at x2").
2. Sort these events.
3. Iterate through the sorted events and maintain an **active state** (e.g., how many overlapping intervals there are at this point).

---

## 2️⃣ Core Variations

### 1D Interval Sweeping
Used for meeting rooms, overlapping intervals, calendar events.
- **Event creation**: For an interval `[start, end]`, create two events: `(start, +1)` and `(end, -1)`.
- **Sorting**: Sort events by their time. If a start and end happen at the same time, carefully decide which should be processed first based on problem constraints (usually process end before start to free up resources).
- **Sweeping**: Iterate through events, keeping a running sum of active intervals.

### 2D Geometric Sweeping
Used for finding intersections of line segments, area of overlapping rectangles.
- Keep track of an active set of line segments.
- Usually requires a Binary Search Tree (like a Red-Black tree in C++ or a sorted list/heap in Python) to keep the active elements sorted by their y-coordinates.

---

## 3️⃣ When to Apply Sweep Line

Think of this technique when:
1. You are dealing with a set of **Intervals** and need to find overlaps, maximum concurrent events, or merge them.
2. The problem involves scheduling (e.g., minimum number of meeting rooms required).
3. The problem involves 2D geometry (intersections, outlines, skyline problem).
4. You need to perform multiple range additions/updates (Similar to Difference Arrays, which is a static form of sweep line).

---

## 4️⃣ Summary
Sweep line transforms complex 2D geometric or 1D overlapping interval problems into a simple sorting problem followed by a linear scan. It typically reduces O(N²) time complexity down to O(N log N) (due to sorting).
