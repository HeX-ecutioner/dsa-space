# 🔢 Bit Manipulation

The **Bit Manipulation** technique involves algorithmically manipulating the bits (0s and 1s) of binary numbers to solve specific problems efficiently.

At the hardware level, all data is represented as binary bits. Bitwise operations are incredibly fast because they are directly supported by the CPU. This technique allows us to achieve optimal time and space complexities, especially when dealing with sets, frequencies, or mathematical properties.

---

## 1️⃣ What is the Bit Manipulation Technique?

Bit manipulation relies on fundamental bitwise operators:
- **AND (`&`)**: 1 if both bits are 1, else 0.
- **OR (`|`)**: 1 if at least one bit is 1, else 0.
- **XOR (`^`)**: 1 if bits are different, 0 if bits are same.
- **NOT (`~`)**: Inverts all bits (0 becomes 1, 1 becomes 0).
- **Left Shift (`<<`)**: Shifts bits to the left, adding 0s on the right (Equivalent to multiplying by 2).
- **Right Shift (`>>`)**: Shifts bits to the right, discarding rightmost bits (Equivalent to dividing by 2).

---

## 2️⃣ Core Principles and Tricks

### The XOR Magic
XOR has some very special properties that are frequently used in competitive programming:
1. `x ^ x = 0` (XORing a number with itself cancels it out)
2. `x ^ 0 = x` (XORing with 0 keeps the number unchanged)
3. XOR is associative and commutative: `a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b`.
- **Use Case**: Finding a single non-repeating element in an array where all others repeat exactly twice.

### Brian Kernighan's Algorithm
`n & (n - 1)` drops the lowest set bit of `n`.
- **Use Case**: Counting the number of 1s in the binary representation of a number in O(k) time, where k is the number of set bits.
- **Use Case**: Checking if a number is a power of 2. (If `n & (n - 1) == 0`, it's a power of 2).

### Bit Masking
Using a number to represent a subset or state. Since a 32-bit integer has 32 bits, we can use it to represent whether up to 32 items are present (1) or absent (0).
- **Check if i-th bit is set**: `(n & (1 << i)) != 0`
- **Set the i-th bit**: `n = n | (1 << i)`
- **Clear the i-th bit**: `n = n & ~(1 << i)`
- **Toggle the i-th bit**: `n = n ^ (1 << i)`

---

## 3️⃣ When to Apply Bit Manipulation

Think of this technique when:
1. The problem involves **powers of 2**.
2. The problem asks you to find a **unique element** among pairs/triplets.
3. You need to **count set bits** or examine binary representations.
4. The constraints are very tight (e.g., O(1) space required) and involve frequencies of integers.
5. You need to generate all subsets (using numbers `0` to `2^n - 1` as masks).

---

## 4️⃣ Summary
Bit manipulation provides highly optimized O(1) or O(log N) solutions to problems that would otherwise require extra space (like Hash Maps) or loops. It relies on a few fundamental tricks that, once mastered, make binary-related problems trivial.
