from linked_list import LinkedList


class Queue:
    """ Linked List implementation """

    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop_first()

    def peek(self):
        return self.queue.head.value

    def traverse(self):
        return self.queue.traverse()


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.traverse())

    queue.dequeue()
    print(queue.peek())
    queue.dequeue()
    print(queue.traverse())

