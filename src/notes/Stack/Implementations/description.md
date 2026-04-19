# Stack Implementations

## Description
This section covers stack implementations using arrays and linked lists.

### Array Stack
- **Static**: Fixed memory allocation, manual index management, O(1) access time
- **Dynamic**: Python list with automatic resizing, grows/shrinks as needed, amortized O(1) operations

### Linked List Stack
- Uses head pointer for O(1) push/pop operations
- No fixed size constraint, but requires extra memory per node for pointers
- Better for variable-size stacks with unpredictable growth patterns

### Comparison
| Feature | Array Stack | Linked List Stack |
|---------|-------------|-------------------|
| Push/Pop | O(1) | O(1) |
| Memory | Contiguous | Scattered |
| Space Overhead | Minimal | Extra pointer per node |

