def evaluate_postfix(expr):
    """
    Evaluate a postfix (Reverse Polish Notation) expression.

    Supported operators: +, -, *, /
    Operands and operators must be space-separated.

    Example:
    "2 3 4 * +" -> 14
    """
    stack = []

    for token in expr.split():
        # If token is an operand, push to stack
        if token.isdigit():
            stack.append(int(token))
        else:
            # Pop operands in correct order
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")

            b = stack.pop()
            a = stack.pop()

            # Apply operator
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("Division by zero")
                stack.append(a // b)  # integer division
            else:
                raise ValueError(f"Unsupported operator: {token}")

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")

    return stack.pop()


# Example usage:

expr1 = "2 3 4 * +"
print(evaluate_postfix(expr1))  # Output: 14
expr2 = "10 2 8 * + 3 -"
print(evaluate_postfix(expr2))  # Output: 23