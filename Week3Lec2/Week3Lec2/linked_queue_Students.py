class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  pass

class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""

  #-------------------------- nested _Node class --------------------------
  class _Node:

    def __init__(self, element, next):
      self._element = element
      self._next = next

  #------------------------------- queue methods -------------------------------
  def __init__(self):
    """Create an empty queue."""
    self._head = None
    self._tail = None
    self._size = 0                          # number of queue elements

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._head._element              # front aligned with head of list

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    # to do
    pass
    
  def enqueue(self, e):
    """Add an element to the back of queue."""
    newest = self._Node(e, None)            
    # to do
    pass

  def printAll(self):
      # print the contents of the Linked List
      # to do
      result =""
      currNode = self._head
      while currNode is not None:
          result += str(currNode._element)+" "
          currNode = currNode._next
    
      return result[:-1]


queue = LinkedQueue()
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(22)
queue.enqueue(35)

print("Queue contents: "+queue.printAll())
print(queue.dequeue())  # 5
print(queue.dequeue())  # 10
print("Queue contents: "+queue.printAll())
