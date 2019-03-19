class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return f"Node(value={self.value})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        nodes = []
        current_node = self.head

        while current_node:
            nodes.append(current_node.value)
            current_node = current_node.next_node

        return ",".join(map(str, nodes))

    def append(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
        else:
            last_node = self.tail
            last_node.next_node = new_node

        self.tail = new_node

    def prepend(self, value):
        new_node = Node(value, next_node=self.head)
        self.head = new_node

    def pop(self):
        """Pop the last element in the list"""
        current_node = self.head
        previous_node = None

        # Iterate through all nodes
        while current_node:
            # When you reach the last node
            if not current_node.next_node:
                # If no previous node, the last node was the head
                if not previous_node:
                    self.head = None
                    self.tail = None
                else:
                    previous_node.next_node = None
                    self.tail = previous_node

                return current_node

            previous_node = current_node
            current_node = current_node.next_node

    def pop_first(self):
        """Pop the first element in the list"""
        current_node = self.head

        if current_node:
            self.head = current_node.next_node

        return current_node

    def remove(self, value):
        """Remove a given node from the list"""
        current_node = self.head
        previous_node = None

        while current_node:
            if current_node.value == value:
                # We are removing the head
                if not previous_node:
                    self.head = current_node.next_node
                # We are removing the tail
                elif not current_node.next_node:
                    previous_node.next_node = None
                    self.tail = previous_node
                else:
                    previous_node.next_node = current_node.next_node
                return current_node

            previous_node = current_node
            current_node = current_node.next_node

    def is_empty(self):
        if self.head:
            return False
        return True


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    print(linked_list.traverse())

    linked_list.remove(1)
    linked_list.remove(2)
    print(linked_list.head.value)
    print(linked_list.tail.value)
    print(linked_list.traverse())

    linked_list.append(4)
    print(linked_list.traverse())

    linked_list.pop()
    linked_list.pop_first()
    print(linked_list.traverse())
