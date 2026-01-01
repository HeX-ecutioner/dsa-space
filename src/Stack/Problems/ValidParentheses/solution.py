def is_valid_parentheses(s: str) -> bool:
    """
    Check if the input string of parentheses is valid.
    
    A string is considered valid if:
    - Open brackets are closed by the same type of brackets.
    - Open brackets are closed in the correct order.
    
    Args:
    s (str): The input string containing parentheses.
    
    Returns:
    bool: True if the string is valid, False otherwise.
    """
    # Stack to keep track of opening brackets
    stack = []
    # Mapping of closing brackets to their corresponding opening brackets
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        # If the character is a closing bracket
        if char in mapping:
            # Pop the topmost element from the stack if it's not empty, else assign a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the popped element matches the corresponding opening bracket
            if mapping[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # If the stack is empty, all opening brackets were matched
    return not stack

# Example usage:
if __name__ == "__main__":
    test_string = "([]{}){}"
    print(f"Is the string '{test_string}' valid? {is_valid_parentheses(test_string)}")