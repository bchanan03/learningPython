from algorithems.stack import stack

if __name__ == "__main__":
    myStack = stack.Stack()
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)

    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())
