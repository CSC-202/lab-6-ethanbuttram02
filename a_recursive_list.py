class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class List:
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
    return data.first == data.last == None

# input : a list, an index position, a value to be inserted
# output: a modified list with a value inserted at the index
def addAtIndex(data: List, index: int, value: int) -> List:
    def helper(v: Node, index: int, i: int):
        if i == index:
            v.next = Node(value, v.next)
            return v
        elif i > index:
            raise IndexError('Index out of Range')
        else:
            return helper(v.next, index, i + 1)

    if isEmpty(data):
        data.first = Node(value, None)
    elif index < 0 or index >= len(data):
        raise IndexError('Index out of Range')
    else:
        helper(data.first, index, 0)
    
    return data


# input : a list
# output: a modified list with the value removed at a specified index
def removeAtIndex(data: List, index: int) -> tuple[Node, List]:
    def helper(v: Node, index: int, i: int):
        if i + 1 == index:
            target: Node = v.next
            v.next = target.next
            return target, data
        elif i > index:
            raise IndexError('Index out of Range')
        else:
            return helper(v.next, index, i + 1)

    if isEmpty(data):
        return None
    elif index < 0 or index >= len(data):
        raise IndexError('Index out of Range')
    return helper(data.first, index, 0), data

# input : a list, a value to be inserted
# output: a modified list with a value inserted at the front
def addToFront(data: List, value: int) -> List:
    data.first = Node(value, data.first)
    return data

# input : a list, a value to be inserted
# output: a modified list with a value inserted at the back
def addToBack(data: List, value: int) -> List:
    addAtIndex(data, len(data) - 1, value)

# input : a list
# output: an element from the specified index
def getElementAtIndex(data: List, index: int) -> Node:
    def helper(v: Node, index: int, i: int):
        if i == index:
            return v
        elif i > index:
            raise IndexError('Index out of Range')
        else:
            return helper(v.next, index, i + 1)

    if isEmpty(data):
        return None
    elif index < 0 or index >= len(data):
        raise IndexError('Index out of Range')
    return helper(data.first, index, 0)

# input : a list
# output: an empty list
def clear(data: List) -> List:
    data.first = None
    return data
