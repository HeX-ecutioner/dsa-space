# Hash Functions

A **Hash Function** is the mathematical algorithm that powers a hash table. It takes an input of arbitrary size (the "key") and maps it to an output of a fixed size (the "hash code" or "index").

## Properties of a Good Hash Function

For a hash table to achieve its theoretical O(1) performance, the hash function must be carefully designed:

1. **Deterministic:** Given the exact same input key, it must *always* produce the exact same output hash code. If `hash("apple") == 5` today, it must equal 5 tomorrow.
2. **Fast to Compute:** The time it takes to compute the hash must be O(1) and inherently fast. If calculating the hash takes O(N) time (where N is the length of the string), looking up the key also takes O(N) time.
3. **Uniform Distribution:** It should map keys uniformly across the entire array, minimizing collisions. It should avoid clustering, even if the input keys are very similar (e.g., "test1", "test2", "test3").
4. **Utilizes the Entire Key:** A good hash function uses all the data in the key to compute the hash.

## Common Hash Function Methods

### 1. Division Method
The simplest approach. We map a key to one of the `M` slots in the array by taking the remainder of the key divided by `M`.
`h(k) = k % M`

*Best Practice:* `M` is usually chosen to be a prime number not too close to a power of 2, which helps break up patterns in the input data.

### 2. Multiplication Method
This method operates in two steps:
1. Multiply the key `k` by a constant `A` (where 0 < A < 1) and extract the fractional part.
2. Multiply that fractional part by `M` (the array size) and take the floor.
`h(k) = floor(M * (k * A % 1))`

The advantage here is that the value of `M` is not as critical, though it's typically chosen as a power of 2 for performance.

### 3. String Hashing (Polynomial Rolling Hash)
When hashing strings, we need to convert the string into an integer. A common method is to treat the string as a polynomial.
For a string `s` of length `n`:
`hash(s) = (s[0] * p^(n-1) + s[1] * p^(n-2) + ... + s[n-1] * p^0) % M`
Where `p` is a prime number (e.g., 31) roughly equal to the number of possible characters, and `M` is a large prime.

## Security vs. Speed
There are two main categories of hash functions:

1. **Non-Cryptographic (Fast):** Used in hash tables and maps. Built purely for speed and uniform distribution. Examples: MurmurHash, CityHash, FNV-1a.
2. **Cryptographic (Secure):** Used for security, passwords, and checksums. Designed to be computationally infeasible to reverse (pre-image resistance) or to find two inputs that produce the same output (collision resistance). Examples: SHA-256, MD5, bcrypt. They are much slower and generally NOT used for hash tables.
