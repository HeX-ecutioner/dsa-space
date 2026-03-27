# Demonstrate the concept of using multiple standard arrays of the same size where the i-th element of each array represents a different attribute of the same entity. (Note: Object-Oriented Programming mostly replaced this, but it is heavily used in high-performance Data Oriented Design / ECS architectures in gaming)

def process_parallel_arrays():
    # Time Complexity: O(n) to iterate
    # Space Complexity: O(n)
    
    # Instead of creating a 'Person' object with name, age, and role,
    # we store them in parallel contiguous blocks of memory for faster CPU caching.
    names =  ["Alice", "Bob", "Charlie"]
    ages =   [25,      30,    35]
    active = [True,    False, True]
    
    active_users = []
    
    # We access the "entity" by using the same index across all arrays
    for i in range(len(names)):
        if active[i]:
            active_users.append(f"{names[i]} ({ages[i]})")
            
    return active_users

if __name__ == "__main__":
    print("Active Users:", process_parallel_arrays()) 
    # Expected: ['Alice (25)', 'Charlie (35)']