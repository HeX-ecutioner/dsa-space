# Stack Representation

## Logical Representation
A stack is a Last In, First Out (LIFO) linear data structure that allows access to only the most recently added element. This means that the last element added to the stack is the first one to be removed. Stacks are commonly used in scenarios such as function call management, expression evaluation, and backtracking algorithms.

## Physical Representation
Stacks can be implemented using two primary data structures:

- **Array**: 
    - Uses contiguous memory allocation.
    - Fixed size, which can lead to overflow if the stack exceeds its capacity.
    - Access time is O(1) for push and pop operations.

- **Linked List**: 
    - Uses scattered memory allocation.
    - Dynamic size, allowing for growth as needed.
    - Each element (node) contains a reference to the next node, making it flexible but with slightly higher overhead for memory management.

## Stack Pointer
The stack pointer is a special pointer that keeps track of the top of the stack. Its movement is as follows:
- **Push Operation**: The stack pointer moves up to point to the new top element after an item is added.
- **Pop Operation**: The stack pointer moves down to point to the previous top element after an item is removed.

## Diagrams and Traces
### Stack Operations Example
1. **Initial Stack**: 
     ```
     [ ]
     ```

2. **Push 1**: 
     ```
     [1]
     ```

3. **Push 2**: 
     ```
     [1, 2]
     ```

4. **Pop Operation**: 
     ```
     [1]  // 2 is removed
     ```

5. **Push 3**: 
     ```
     [1, 3]
     ```

### Stack Pointer Movement
- After pushing 1: Stack Pointer -> 1
- After pushing 2: Stack Pointer -> 2
- After popping: Stack Pointer -> 1
- After pushing 3: Stack Pointer -> 3

