class Node:  # Node class represents a single element in the linked list.
    def __init__(self, data):
        self.data = data  # The value stored
        self.next = None  # Pointer/reference to the next node


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Points to first node
        self.tail = None  # Optional: track last node for O(1) insert at end
        self.size = 0  # Track number of elements

    # ----------------------------
    # INSERTION OPERATIONS
    # ----------------------------

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Point new node to curr head
        self.head = new_node  # Update head

        if self.tail is None:  # If list was empty
            self.tail = new_node

        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def insert_at_position(self, data, position):
        if position < 0 or position > self.size:
            print("Invalid position")
            return

        if position == 0:
            self.insert_at_beginning(data)
            return

        if position == self.size:
            self.insert_at_end(data)
            return

        new_node = Node(data)
        curr = self.head

        for _ in range(position - 1):
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node

        self.size += 1

    # ----------------------------
    # DELETION OPERATIONS
    # ----------------------------

    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.size -= 1

    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = self.tail = None
            self.size -= 1
            return

        curr = self.head
        while curr.next.next:
            curr = curr.next

        curr.next = None
        self.tail = curr
        self.size -= 1

    def delete_by_value(self, value):
        curr = self.head
        prev = None

        while curr:
            if curr.data == value:
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next

                if curr == self.tail:
                    self.tail = prev

                self.size -= 1
                return

            prev, curr = curr, curr.next

        print("Value not found")

    # ----------------------------
    # UTILITY OPERATIONS
    # ----------------------------

    def search(self, value):
        curr = self.head
        index = 0

        while curr:
            if curr.data == value:
                return index
            curr = curr.next
            index += 1

        return -1

    def display(self):
        curr = self.head
        result = []

        while curr:
            result.append(str(curr.data))
            curr = curr.next

        print(" -> ".join(result) + " -> null" if result else "null")

    def reverse(self):  # Reverse the linked list
        prev, curr = None, self.head
        self.tail = self.head

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        self.head = prev

    def find_middle(self):  # Using fast/slow pointer technique
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data if slow else None

    def get_size(self):
        return self.size  # Return the number of elements in the list


def main():
    sll = SinglyLinkedList()

    while True:
        print(
            "\n--- Singly Linked List Menu ---\n1. Insert at Beginning\n2. Insert at End\n3. Insert at Position\n4. Delete from Beginning"
            "\n5. Delete from End\n6. Delete by Value\n7. Search\n8. Display\n9. Reverse\n10. Find Middle\n11. Size\n0. Exit"
        )

        ch = input("\nEnter choice: ").strip()

        try:
            if ch == "1":
                val = int(input("Enter value: "))
                sll.insert_at_beginning(val)
                print(f"✅ Inserted {val} at beginning")

            elif ch == "2":
                val = int(input("Enter value: "))
                sll.insert_at_end(val)
                print(f"✅ Inserted {val} at end")

            elif ch == "3":
                val = int(input("Enter value: "))
                pos = int(input("Enter position: "))
                sll.insert_at_position(val, pos - 1)
                print(f"✅ Inserted {val} at position {pos}")

            elif ch == "4":
                if sll.get_size() == 0:
                    print("❌ List is empty")
                else:
                    print("Before:", end=" ")
                    sll.display()
                    sll.delete_from_beginning()
                    print("✅ Deleted from beginning")
                    print("After:", end=" ")
                    sll.display()

            elif ch == "5":
                if sll.get_size() == 0:
                    print("❌ List is empty")
                else:
                    print("Before:", end=" ")
                    sll.display()
                    sll.delete_from_end()
                    print("✅ Deleted from end")
                    print("After:", end=" ")
                    sll.display()

            elif ch == "6":
                val = int(input("Enter value: "))
                if sll.get_size() == 0:
                    print("❌ List is empty")
                else:
                    print("Before:", end=" ")
                    sll.display()
                    sll.delete_by_value(val)
                    print(f"✅ Attempted deletion of {val}")
                    print("After:", end=" ")
                    sll.display()

            elif ch == "7":
                val = int(input("Enter value: "))
                index = sll.search(val)
                if index != -1:
                    print(f"✅ Value {val} found at index {index}")
                else:
                    print(f"❌ Value {val} not found")

            elif ch == "8":
                print("📋 Current List:", end=" ")
                sll.display()

            elif ch == "9":
                print("Before:", end=" ")
                sll.display()
                sll.reverse()
                print("✅ List reversed")
                print("After:", end=" ")
                sll.display()

            elif ch == "10":
                mid = sll.find_middle()
                if mid is not None:
                    print(f"📍 Middle element: {mid}")
                else:
                    print("❌ List is empty")

            elif ch == "11":
                print(f"📏 Size of list: {sll.get_size()}")

            elif ch == "0":
                print("👋 Exiting... Goodbye!")
                break

            else:
                print("❌ Invalid choice. Please try again.")

        except ValueError:
            print("❌ Invalid input. Please enter numeric values where required.")


if __name__ == "__main__":
    main()