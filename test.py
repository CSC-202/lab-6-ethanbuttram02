import a_recursive_list as List
import b_recursive_stack as Stack
import c_recursive_queue as Queue

l = List.initialize()
s = Stack.initialize()
q = Queue.initialize()

# LIST TESTS
# Empty test
if List.isEmpty(l):
    print('PASSED - List is empty')
else:
    print('FAILED - List is not empty')
if Stack.isEmpty(s):
    print('PASSED - Stack is empty')
else:
    print('FAILED - Stack is not empty')
if Queue.isEmpty(q):
    print('PASSED - Queue is empty')
else:
    print('FAILED - Queue is not empty')

# addAtIndex test
print('Begin List Tests')
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

# STACK TESTS

# QUEUE TESTS

# Clear test
List.clear(l)
Stack.clear(s)
Queue.clear(q)

if len(l) == 0:
    print('PASSED - List is clear')
else:
    print('FAILED - List is not clear')
if len(s) == 0:
    print('PASSED - Stack is clear')
else:
    print('FAILED - Stack is not clear')
if len(q) == 0:
    print('PASSED - Queue is clear')
else:
    print('FAILED - Queue is not clear')


