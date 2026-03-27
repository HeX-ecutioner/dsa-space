class Node:
    def __init__(self, data):
        self.data = data
        self.npx = 0  # XOR of prev and next node ids


class XORLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__nodes = {}  # Dictionary to simulate memory
        self.size = 0

    def _xor(self, a, b):
        return a ^ b

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_id = id(new_node)

        self.__nodes[new_id] = new_node

        if self.head is None:
            self.head = self.tail = new_node
        else:
            head_id = id(self.head)

            new_node.npx = head_id
            self.head.npx ^= new_id

            self.head = new_node

        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        new_id = id(new_node)

        self.__nodes[new_id] = new_node

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            tail_id = id(self.tail)

            new_node.npx = tail_id
            self.tail.npx ^= new_id

            self.tail = new_node

        self.size += 1

    def display(self):
        print("\n📋 XOR Linked List:")

        curr = self.head
        prev_id = 0

        while curr:
            print(curr.data, end=" -> ")

            next_id = self._xor(prev_id, curr.npx)

            prev_id = id(curr)
            curr = self.__nodes.get(next_id)

        print("None")

    def search(self, value):
        curr = self.head
        prev_id = 0

        while curr:
            if curr.data == value:
                return True

            next_id = self._xor(prev_id, curr.npx)
            prev_id = id(curr)
            curr = self.__nodes.get(next_id)

        return False

    def get_size(self):
        return self.size


def main():
    xll = XORLinkedList()

    while True:
        print(
            "\n--- XOR Linked List Menu ---\n1. Insert at Beginning\n2. Insert at End\n3. Search\n4. Display\n5. Size\n6. Exit"
        )

        ch = input("\nEnter choice: ").strip()

        try:
            if ch == "1":
                val = int(input("Enter value: "))
                xll.insert_at_beginning(val)
                print(f"✅ Inserted {val} at beginning")

            elif ch == "2":
                val = int(input("Enter value: "))
                xll.insert_at_end(val)
                print(f"✅ Inserted {val} at end")

            elif ch == "3":
                val = int(input("Enter value: "))
                found = xll.search(val)
                print("✅ Found" if found else "❌ Not found")

            elif ch == "4":
                xll.display()

            elif ch == "5":
                print(f"📏 Size: {xll.get_size()}")

            elif ch == "6":
                print("👋 Exiting...")
                break

            else:
                print("❌ Invalid choice")

        except ValueError:
            print("❌ Invalid input")


if __name__ == "__main__":
    main()  # Example usage
