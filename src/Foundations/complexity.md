# 🚀 Time & Space Complexity

## 📌 1. What is Time Complexity?

**Time complexity** measures how the number of operations grows with input size `n`.

> It answers: *“How does runtime scale?”*

We focus on **trend**, not exact time.

### ⚙️ Formal Definition

If an algorithm performs `f(n)` operations, we express:

```
T(n) = O(f(n))
```

## 🧠 Why We Ignore Constants & Lower Terms

### Example:

```
T(n) = 5n² + 3n + 10
```

➡️ Dominant term = `n²`
➡️ Final complexity:

```
O(n²)
```

### Reason:

As `n → ∞`, smaller terms become negligible.

## 📊 Growth Rate Visualization (Important Intuition)

| n    | log n | n    | n log n | n²     | 2ⁿ   |
| ---- | ----- | ---- | ------- | ------ | ---- |
| 10   | 3     | 10   | 33      | 100    | 1024 |
| 100  | 7     | 100  | 664     | 10,000 | 🔥   |
| 1000 | 10    | 1000 | 9965    | 1e6    | 💀   |

👉 Exponential explodes insanely fast.

## 🧩 Common Complexity Classes (With Examples)

### 🟢 O(1) — Constant Time

```cpp
int x = arr[5];
```

✔ Independent of input size

---

### 🔵 O(log n) — Logarithmic

```cpp
binary_search(arr.begin(), arr.end(), x);
```

📌 Each step halves the problem

---

### 🟡 O(n) — Linear

```cpp
for(int i=0; i<n; i++)
```

---

### 🟠 O(n log n)

```cpp
sort(arr.begin(), arr.end());
```

📌 Seen in:

* Merge Sort
* Heap Sort
* Quick Sort (average)

---

### 🔴 O(n²) — Quadratic

```cpp
for(i)
  for(j)
```

📌 Common in:

* Bubble Sort
* Selection Sort

---

### ⚫ O(2ⁿ) — Exponential

```cpp
generate all subsets
```

---

### ☠️ O(n!) — Factorial

```cpp
generate all permutations
```

## 🧮 How to Calculate Time Complexity

### 1️⃣ Loops

```cpp
for(int i=0; i<n; i++)   // O(n)
```

---

### 2️⃣ Nested Loops

```cpp
for(i=0;i<n;i++)
  for(j=0;j<n;j++)
```

➡️ `O(n²)`

---

### 3️⃣ Dependent Loops

```cpp
for(i=0;i<n;i++)
  for(j=0;j<i;j++)
```

➡️ `O(n(n+1)/2) = O(n²)`

---

### 4️⃣ Logarithmic Loops

```cpp
for(int i=1; i<n; i*=2)
```

➡️ `O(log n)`

---

### 5️⃣ Recursion

#### Example:

```cpp
T(n) = T(n/2) + O(1)
```

➡️ `O(log n)`

## 🔁 Recurrence Relations & Master Theorem

### General form:

```
T(n) = aT(n/b) + f(n)
```

---

### 🧠 Master Theorem

| Case | Condition         | Result              |
| ---- | ----------------- | ------------------- |
| 1    | f(n) < n^log_b(a) | O(n^log_b(a))       |
| 2    | f(n) = n^log_b(a) | O(n^log_b(a) log n) |
| 3    | f(n) > n^log_b(a) | O(f(n))             |

---

### Example:

```
T(n) = 2T(n/2) + n
```

➡️ `O(n log n)`

## 📦 Space Complexity Deep Dive

### Types:

| Type            | Meaning          |
| --------------- | ---------------- |
| Input Space     | Memory for input |
| Auxiliary Space | Extra memory     |

---

### Example:

```cpp
int sum(int arr[], int n)
```

➡️ O(1) auxiliary space

---

### Recursion Stack Space

```cpp
factorial(n)
```

➡️ O(n) stack space

## ⚖️ Time vs Space Tradeoff

| Approach       | Time | Space |
| -------------- | ---- | ----- |
| Brute Force    | High | Low   |
| Optimized (DP) | Low  | High  |

### Example:

* Fibonacci

  * Recursive → O(2ⁿ), O(n)
  * DP → O(n), O(n)

## 📉 Amortized Complexity

Used when operations vary.

### Example: Dynamic Array (vector)

* Push: mostly O(1)
* Resize: O(n)

➡️ Amortized = **O(1)**

## 🔄 Best, Average, Worst Case

| Case    | Meaning      |
| ------- | ------------ |
| Best    | Ideal input  |
| Average | Expected     |
| Worst   | Maximum time |

---

### Example: Quick Sort

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(n log n) |
| Average | O(n log n) |
| Worst   | O(n²)      |

## ⚡ Practical Complexity Benchmarks

| Operations/sec ≈ 10⁸ |

| n   | Max Complexity |
| --- | -------------- |
| 10⁸ | O(1)           |
| 10⁷ | O(n)           |
| 10⁵ | O(n log n)     |
| 10³ | O(n²)          |

## 🧠 Hidden Complexity (Important)

### STL Examples:

| Function       | Complexity |
| -------------- | ---------- |
| sort()         | O(n log n) |
| map insert     | O(log n)   |
| unordered_map  | O(1) avg   |
| priority_queue | O(log n)   |

## 🎯 Optimization Mindset

Ask yourself:

* Can I reduce nested loops?
* Can I precompute?
* Can I use hashing?
* Can I sort first?
* Can I use binary search?