class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = StackNode(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.head is None:
            return

        data = self.head.data
        self.head = self.head.next
        return data

    def __str__(self):
        temp = self.head
        s = ""
        while temp:
            s += str(temp.data) + " -> "
            temp = temp.next
        s += "None"
        return s
