from exceptions import Empty

from array_stack import ArrayStack

class QueueUsingStacks:
    def __init__(self):
        self._stack1 = ArrayStack()
        self._stack2 = ArrayStack()

    def __len__(self):
        return len(self._stack1)
    

    def is_empty(self):
        return len(self._stack1)==0

    def enqueue(self,e):
        self._stack1.push(e)

    def dequeue(self):
        while len(self._stack1)!= 1:
            self._stack2.push(self._stack1.pop())
        self._stack1.pop()
        while len (self._stack2) != 0:
            self._stack1.push(self._stack2.pop())



def checkQueue():
    queue1 = QueueUsingStacks()
    queue1.enqueue(3)
    queue1.enqueue(5)
    queue1.enqueue(7)
    queue1.enqueue(9)
    print("1. Length of Queue ",len(queue1))

    print(queue1.dequeue())

    print("2. Length of Queue",len(queue1))

    queue1.enqueue(20)

    print("3. Length of Queue",len(queue1))

    print(queue1.dequeue())

    print("4. Length of Queue",len(queue1))


checkQueue()
