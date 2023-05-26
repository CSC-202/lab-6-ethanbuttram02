import a_recursive_list as List
import b_recursive_stack as Stack
import c_recursive_queue as Queue

l = List.initialize()
s = Stack.initialize()
q = Queue.initialize()

# LIST TESTS
print('Begin List Tests')

# empty test
if List.isEmpty(l):
    print('PASSED - List is empty')
else:
    print('FAILED - List is not empty')

# addAtIndex test
List.addAtIndex(l, 0, 1)
if l.toPythonList() == [1]:
    print('PASSED - Added 1 at index 0 of the list')
else:
    print('FAILED - addAtIndex')

# addToFront test
List.addToFront(l, 2)
if l.toPythonList() == [2, 1]:
    print('PASSED - Added 2 to the front of the list')
else:
    print('FAILED - addToFront')

# addToBack test
List.addToBack(l, 5)
if l.toPythonList() == [2, 1, 5]:
    print('PASSED - Added 5 to the back of the list')
else:
    print('FAILED - addToBack')

# removeAtIndex test
List.removeAtIndex(l, 1)
if l.toPythonList() == [2, 5]:
    print('PASSED - Removed 1 from the list')
else:
    print('FAILED - removeAtIndex')

# getElementAtIndex test
if List.getElementAtIndex(l, 1).value == 5:
    print('PASSED - Obtained the value 5 at index 1')
else:
    print('FAILED - getElementAtIndex')

# Clear test
List.clear(l)
if len(l) == 0:
    print('PASSED - List is clear')
else:
    print('FAILED - List is not clear')





# STACK TESTS
print('\nBegin Stack tests')

# empty test
if Stack.isEmpty(s):
    print('PASSED - Stack is empty')
else:
    print('FAILED - Stack is not empty')

# push test
Stack.push(s, 2)
Stack.push(s, 3)
Stack.push(s, 5)
if s.toPythonList() == [5, 3, 2]:
    print('PASSED - 2, 3, and 5 pushed to the stack')
else:
    print('FAILED - push')

# pop test
popped = Stack.pop(s)
if s.toPythonList() == [3, 2]:
    print('PASSED - Popped 5 from the stack')
else:
    print('FAILED - Pop')
if popped[0].value == 5:
    print('PASSED - Popped 5 from the stack')
else:
    print('FAILED - Pop: Node retrieval')

# peek test
Stack.peek(s) # for no accidental pop
if s.toPythonList() == [3, 2]:
    print('PASSED - Peeked at 3 from the stack')
else:
    print('FAILED - Peek')
if Stack.peek(s).value == 3:
    print('PASSED - Peeked at 3 from the stack')
else:
    print('FAILED - Peek: value retrieval')

# clear test
Stack.clear(s)
if len(s) == 0:
    print('PASSED - Stack is clear')
else:
    print('FAILED - Stack is not clear')


# QUEUE TESTS
print('\nBegin Queue Tests')

# empty tests
if Queue.isEmpty(q):
    print('PASSED - Queue is empty')
else:
    print('FAILED - Queue is not empty')

# TODO: Write the tests and implement these functions
# enqueue test
# dequeue test
# peek test

# Clear test
Queue.clear(q)



if len(q) == 0:
    print('PASSED - Queue is clear')
else:
    print('FAILED - Queue is not clear')


