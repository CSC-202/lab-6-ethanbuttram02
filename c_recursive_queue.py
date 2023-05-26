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


def initialize() -> Queue:
    return Queue()


def isEmpty(data: Queue) -> bool:
    return data.first == data.last == None


def enqueue(data: Queue, value: int) -> Queue:
    if isEmpty(data):
        data.first = data.last = Node(value, None)
    else:
        data.last.next = Node(value, None)
        data.last = data.last.next
    return data


def dequeue(data: Queue) -> tuple[Node, Queue]:
    if isEmpty(data):
        raise IndexError('Queue is empty')
    dequeuedNode = data.first
    data.first = data.first.next
    return dequeuedNode, data


def peek(data: Queue) -> Node:
    return data.first


def clear(data: Queue) -> Queue:
    data.first = data.last = None
    return data
