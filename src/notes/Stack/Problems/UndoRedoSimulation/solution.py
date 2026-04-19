class UndoRedo:
    def __init__(self):
        """
        Initialize two stacks:
        - undo: stores executed actions
        - redo: stores undone actions
        """
        self.undo = []
        self.redo = []

    def do(self, action):
        """
        Perform a new action.
        New actions invalidate redo history.
        """
        self.undo.append(action)
        self.redo.clear()

    def undo_action(self):
        """
        Undo the last action.
        Moves the action from undo stack to redo stack.
        """
        if not self.undo:
            print("Nothing to undo")
            return None

        action = self.undo.pop()
        self.redo.append(action)
        return action

    def redo_action(self):
        """
        Redo the last undone action.
        Moves the action from redo stack back to undo stack.
        """
        if not self.redo:
            print("Nothing to redo")
            return None

        action = self.redo.pop()
        self.undo.append(action)
        return action

    def current_state(self): # Return the list of actions currently applied
        return list(self.undo)
    
    
# Example usage:
ur = UndoRedo()
ur.do("Type 'Hello'")
ur.do("Type 'World'")
ur.do("Delete 'World'")

print("Current state:", ur.current_state()) # Output: ["Type 'Hello'", "Type 'World'", "Delete 'World'"]

ur.undo_action()
print("After undo:", ur.current_state()) # Output: ["Type 'Hello'", "Type 'World'"]

ur.undo_action()
print("After undo:", ur.current_state()) # Output: ["Type 'Hello'"]

ur.redo_action()
print("After redo:", ur.current_state()) # Output: ["Type 'Hello'", "Type 'World'"]

ur.do("Type '!'")
print("After new action:", ur.current_state()) # Output: ["Type 'Hello'", "Type 'World'", "Type '!'"]