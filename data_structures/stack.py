from linked_list import LinkedList


class Stack:
    """ Linked List implementation """

    def __init__(self):
        self.stack = LinkedList()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack.tail.value

    def traverse(self):
        return self.stack.traverse()


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.traverse())

    stack.pop()
    print(stack.traverse())

    print(stack.peek())
    print(stack.traverse())
