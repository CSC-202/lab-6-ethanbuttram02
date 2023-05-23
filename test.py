import a_recursive_list as List
import b_recursive_stack as Stack
import c_recursive_queue as Queue

l = List.initialize()
s = Stack.initialize()
q = Queue.initialize()

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
List.addAtIndex(l, 0, 1)
if l.toPythonList() == [1]:
    print('PASSED - addAtIndex')
else:
    print('FAILED - addAtIndex')

List.addToFront(l, 2)
print(l.toPythonList())
if l.toPythonList() == [1, 2]:
    print('PASSED - addToFront')
else:
    print('FAILED - addToFront')

List.addToBack(l, 5)
if l.toPythonList() == [5, 1, 2]:
    print('PASSED - addToBack')
else:
    print('FAILED - addToBack')


List.clear(l)
Stack.clear(s)
Queue.clear(q)

# Clear test
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


