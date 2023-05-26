class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Queue:
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
# output : an empty queue
def initialize() -> Queue:
    return Queue()

# input : a queue
# output : True or false if the queue is empty
def isEmpty(data: Queue) -> bool:
    return data.first == data.last == None

# input : a queue and a value
# output : a modified queue with the value at the back of the queue
def enqueue(data: Queue, value: int) -> Queue:
    if isEmpty(data):
        data.first = data.last = Node(value, None)
    else:
        data.last.next = Node(value, None)
        data.last = data.last.next
    return data

# input : a queue
# output : a tuple containing the removed node and the modified queue
def dequeue(data: Queue) -> tuple[Node, Queue]:
    if isEmpty(data):
        raise IndexError('Queue is empty')
    dequeuedNode = data.first
    data.first = data.first.next
    return dequeuedNode, data

# input : a queue
# output : a node that is the front of the queue
def peek(data: Queue) -> Node:
    return data.first

# input : a queue
# output : an empty queue
def clear(data: Queue) -> Queue:
    data.first = data.last = None
    return data
