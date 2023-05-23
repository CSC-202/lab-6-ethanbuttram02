class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class List:
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

# output: an empty list
def initialize() -> List:
    return List()

# input : a list
# output: true if the list is empty, false if the list is not
def isEmpty(data: List) -> bool:
    return data.head == None

# input : a list, an index position, a value to be inserted
# output: a modified list with a value inserted at the index
def addAtIndex(data: List, index: int, value: int) -> List:
    if data.head == None:
        data.head = Node(value, None)
        return data
    if index == 0:
        data.head = Node(value, data.head.next)
        return data
    if index == 1:
        data.head.next = Node(value, data.head.next)
        return data
    return addAtIndex(data.head.next, index - 1, value)

# input : a list
# output: a modified list with the value removed at a specified index
def removeAtIndex(data: List, index: int) -> tuple[Node, List]:
    if data.head == None:
        raise IndexError('List is empty')
    if index == 1:
        if data.head.next == None:
            raise IndexError('Index out of range')
        nodeReturn = data.head.next
        data.head.next = data.head.next.next
        return (nodeReturn, data)
    return removeAtIndex(data.head.next, index-1)

# input : a list, a value to be inserted
# output: a modified list with a value inserted at the front
def addToFront(data: List, value: int) -> List:
    addAtIndex(data, 0, value)

# input : a list, a value to be inserted
# output: a modified list with a value inserted at the back
def addToBack(data: List, value: int) -> List:
    def helpMePls(data) -> int: # this will give me the length of the List
        if isEmpty(data):
            return 0
        length = 1
        while data.head.next != None:
            length += 1
        return length
    addAtIndex(data, helpMePls(data) - 1, value)

# input : a list
# output: an element from the specified index
def getElementAtIndex(data: List, index: int) -> Node:
    if index == 0:
        return data.head
    return getElementAtIndex(data.head.next, index - 1)

# input : a list
# output: an empty list
def clear(data: List) -> List:
    data.head = None
    return data
