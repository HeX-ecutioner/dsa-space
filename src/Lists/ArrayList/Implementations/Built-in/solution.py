# Built-in Dynamic Array Usage

def demonstrate_builtin():
    # Time Complexity: O(1) amortized append, O(n) insert/delete middle
    # Space Complexity: O(n)
    
    # Python's list is a highly optimized dynamic array under the hood
    arr = []
    
    # O(1) amortized insertions at the end
    arr.append(10)
    arr.append(20)
    arr.append(30)
    
    # O(n) insertion in the middle (shifts elements)
    arr.insert(1, 15)
    
    # O(1) random access
    val = arr[2]
    
    return arr, val

if __name__ == "__main__":
    final_arr, accessed_val = demonstrate_builtin()
    print("Built-in Array:", final_arr) # Expected: [10, 15, 20, 30]
    print("Accessed Index 2:", accessed_val) # Expected: 20