# Queue Representation

## Logical Representation

A queue is a First In, First Out (FIFO) linear data structure that allows access to elements in the exact order they are inserted. This means that the first element added to the queue is the first one to be removed. Queues are widely used in scheduling, buffering, and traversal algorithms such as breadth-first search (BFS).

## Physical Representation

Queues can be implemented using multiple underlying data structures:

* **Array**:

  * Uses contiguous memory allocation.
  * Can be implemented as a linear array or a circular array.
  * Without circular logic, unused space may appear after dequeuing.
  * Enqueue and dequeue operations run in O(1) time with proper pointer management.

* **Linked List**:

  * Uses non-contiguous (scattered) memory allocation.
  * Dynamic size, allowing the queue to grow and shrink as needed.
  * Maintains both front and rear pointers for efficient insertion and removal.
  * Slightly higher memory overhead due to pointer storage.

## Front and Rear Pointers

Queues rely on two pointers to manage operations:

* **Front Pointer**:

  * Points to the element that will be removed next.
  * Advances forward during dequeue operations.

* **Rear Pointer**:

  * Points to the position where new elements are inserted.
  * Advances forward during enqueue operations.

Pointer movement ensures that elements are processed in strict FIFO order.

## Diagrams and Traces

### Queue Operations Example

1. **Initial Queue**:

   ```
   [ ]
   ```

2. **Enqueue 1**:

   ```
   [1]
   ```

3. **Enqueue 2**:

   ```
   [1, 2]
   ```

4. **Dequeue Operation**:

   ```
   [2]  // 1 is removed
   ```

5. **Enqueue 3**:

   ```
   [2, 3]
   ```

### Front and Rear Pointer Movement

* After enqueuing 1: Front -> 1, Rear -> 1
* After enqueuing 2: Front -> 1, Rear -> 2
* After dequeuing: Front -> 2, Rear -> 2
* After enqueuing 3: Front -> 2, Rear -> 3