from algorithems.queue.queue_node import queue_node


class queue:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def push(self, data):
        node = queue_node(data)
        if self.head is None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1

    def pop(self):
        if self.head is None:
            return
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.head is None:
            return
        return self.head.data

    def printQueue(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def __str__(self):
        temp = self.head
        s = ""
        while temp:
            s += str(temp.data) + " -> "
            temp = temp.next
        s += "None"
        return s
