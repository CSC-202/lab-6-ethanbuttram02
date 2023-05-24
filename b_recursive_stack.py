class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
    first: Node
    last: Node

    def __init__(self):
        self.first = None
        self.last = None

    def __len__(self):
        n: int = 0
        current = self.first
        while current != None:
            n += 1
            current = current.next
        return n

    def toPythonList(self):
        result: list = []
        current = self.first
        while current != None:
            result.append(current.value)
            current = current.next
        return result

# input : nothing
# output : an empty stack
def initialize() -> Stack:
    return Stack()

# input : a stack
# output : True if the stack is empty, false otherwise
def isEmpty(data: Stack) -> bool:
    return data.first == data.last == None

# input : a stack and a value
# output : a modified stack with a new value on the top
def push(data: Stack, value: int) -> Stack:
    if isEmpty(data):
        data.first = data.last = Node(value, None)
        return data
    data.last = Node(value, data.last)
    return data
    
# input : stack
# output : a tuple containing the top node of the stack and the modified stack with the top removed
def pop(data: Stack) -> tuple[Node, Stack]:
    poppedNode = data.last
    data.last = data.last.next
    return poppedNode, data

# input : a stack
# output : the top of the stack
def peek(data: Stack) -> Node:
    return data.last

# input : a stack
# output : an empty stack
def clear(data: Stack) -> Stack:
    data.first = data.last = None
    return data
