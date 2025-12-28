# Problem: Determine if repeatedly summing squares of digits reaches 1 -> happy number.
def sum_of_squares(n: int) -> int:
    s = 0
    while n:
        d = n % 10
        s += d*d
        n //= 10
    return s

def is_happy(n: int) -> bool:
    """
    Use Floyd's cycle detection:
    - slow = f(n), fast = f(f(n))
    - if fast becomes 1, happy; if slow==fast then cycle -> unhappy
    Time: O(log n) per iteration, overall small constant for base 10 digits.
    """
    slow = n
    fast = n
    while True:
        slow = sum_of_squares(slow)
        fast = sum_of_squares(sum_of_squares(fast))
        if slow == 1 or fast == 1:
            return True
        if slow == fast:
            return False

# Example usage:
print(is_happy(19))  # Output: True
print(is_happy(2))   # Output: False