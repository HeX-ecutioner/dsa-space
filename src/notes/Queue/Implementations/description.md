# Queue Implementations

## Description
This section covers queue implementations using arrays and linked lists, focusing on
First In, First Out (FIFO) behavior and efficient insertion and removal.

### Array Queue
- **Static / Linear**: Fixed memory allocation with front and rear indices; may waste space after dequeues
- **Circular**: Uses modulo arithmetic to reuse freed space efficiently, O(1) enqueue/dequeue
- **Dynamic**: Python list or deque with automatic resizing, amortized O(1) operations

### Linked List Queue
- Uses both front and rear pointers for O(1) enqueue and dequeue operations
- No fixed size constraint, grows dynamically as elements are added
- Requires extra memory per node due to pointer storage

### Comparison
| Feature | Array Queue | Linked List Queue |
|-------|-------------|-------------------|
| Enqueue/Dequeue | O(1) | O(1) |
| Memory | Contiguous | Scattered |
| Space Overhead | Minimal | Extra pointer per node |
| Reusability | Requires circular logic | Automatic |
