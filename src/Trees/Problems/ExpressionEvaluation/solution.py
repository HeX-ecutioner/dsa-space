"""
Problem: Expression Tree Evaluation
Statement: Given a post-fix expression (Reverse Polish Notation), build and evaluate 
an Expression Tree to handle nested precedence naturally.
"""

class ExpNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    # Time Complexity: O(N) to build and O(N) to evaluate.
    # Space Complexity: O(N) to store the tree.

    def build_tree(self, postfix_tokens):
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in postfix_tokens:
            node = ExpNode(token)
            if token in operators:
                # Operators take the top two elements from the stack as children
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
            
        return stack[0] # The root of the expression tree

    def evaluate(self, node):
        if not node: return 0
        
        # If it's a leaf (a number), return its integer value
        if not node.left and not node.right:
            return int(node.value)
            
        # Recursively evaluate subtrees
        left_val = self.evaluate(node.left)
        right_val = self.evaluate(node.right)
        
        if node.value == '+': return left_val + right_val
        if node.value == '-': return left_val - right_val
        if node.value == '*': return left_val * right_val
        if node.value == '/': return left_val / right_val

if __name__ == "__main__":
    # Represents (5 + 3) * 4
    tokens = ["5", "3", "+", "4", "*"]
    et = ExpressionTree()
    root = et.build_tree(tokens)
    print("Evaluation Result:", et.evaluate(root)) # Expected: 32