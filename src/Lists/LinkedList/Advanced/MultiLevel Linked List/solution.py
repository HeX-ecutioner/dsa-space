# Multi-Level Linked List

class Node:
    # Each node has:
    # - data
    # - next pointer (same level)
    # - child pointer (lower level)
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None


class MultiLevelLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node

    def add_child(self, parent_value, child_value):
        # Find parent node
        parent = self._find(self.head, parent_value)

        if parent is None:
            print("❌ Parent not found")
            return

        new_node = Node(child_value)

        # Add child at beginning of child list
        new_node.next = parent.child
        parent.child = new_node

    def _find(self, node, value):
        # DFS search across levels
        while node:
            if node.data == value:
                return node

            # Search in child first
            found = self._find(node.child, value)
            if found:
                return found

            node = node.next

        return None

    def display(self):
        def dfs(node, level):
            while node:
                print("  " * level + str(node.data))
                if node.child:
                    dfs(node.child, level + 1)
                node = node.next

        dfs(self.head, 0)

    def flatten(self):
        if not self.head:
            return

        stack = []
        curr = self.head

        while curr:
            if curr.child:
                # If next exists, save it
                if curr.next:
                    stack.append(curr.next)

                # Move child to next
                curr.next = curr.child
                curr.child = None

            if curr.next is None and stack:
                curr.next = stack.pop()

            curr = curr.next

    def display_flat(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")


def main():
    mll = MultiLevelLinkedList()

    while True:
        print(
            "--- Multi-Level Linked List ---\n1. Insert (main level)\n2. Add Child\n3. Display (hierarchical)\n"
            "4. Flatten\n5. Display Flat\n6. Exit\n"
        )

        ch = input("Choice: ").strip()

        try:
            if ch == "1":
                mll.insert(int(input("Value: ")))

            elif ch == "2":
                p = int(input("Parent value: "))
                c = int(input("Child value: "))
                mll.add_child(p, c)

            elif ch == "3":
                mll.display()

            elif ch == "4":
                mll.flatten()
                print("✅ Flattened")

            elif ch == "5":
                mll.display_flat()

            elif ch == "6":
                print("👋 Exiting...")
                break
            else:
                print("❌ Invalid choice")
        
        except ValueError:
            print("❌ Invalid input")

if __name__ == "__main__":
    main() # Example usage