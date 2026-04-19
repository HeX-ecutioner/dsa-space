def infix_to_postfix(expr):
    """
    Convert an infix expression to postfix expression.

    Supported operators: +, -, *, /
    Operands must be single-letter or single-digit.
    Parentheses are supported.

    Example:
    "A+B*C" -> "ABC*+"
    """

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    output = []

    for ch in expr:
        # If operand, add to output
        if ch.isalnum():
            output.append(ch)

        # If opening parenthesis, push to stack
        elif ch == '(':
            stack.append(ch)

        # If closing parenthesis, pop until '('
        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Mismatched parentheses")
            stack.pop()  # remove '('

        # If operator
        else:
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence.get(ch, 0)):
                output.append(stack.pop())
            stack.append(ch)

    # Pop remaining operators
    while stack:
        if stack[-1] == '(':
            raise ValueError("Mismatched parentheses")
        output.append(stack.pop())

    return ''.join(output)


# Example usage:

print(infix_to_postfix("A+B*C")) # Output: ABC*+
print(infix_to_postfix("(A+B)*C")) # Output: AB+C*
print(infix_to_postfix("A+B*C-D/E")) # Output: ABC*+DE/-
print(infix_to_postfix("((A+B)*C-D)*E")) # Output: AB+C*D-E*