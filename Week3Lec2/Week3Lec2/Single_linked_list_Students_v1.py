class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  pass


class Node:
    
  def __init__(self, element, next = None):   # initialize node's fields
    self._element = element               # reference to user's element
    self._next = next                     # reference to next node


class Single_Linked_List:
  #------------------------------- Single Linked List methods -------------------------------
  def __init__(self):
    """Create an empty LinkedList."""
    self._head = None                       # reference to the head node
    self._size = 0                          # number of elements in the list

  def __len__(self):
    """Return the number of elements in the LinkedList."""
    return self._size

  def is_empty(self):
    """Return True if the LinkedList is empty."""
    return self._size == 0

  def insertAtFirst(self, e):
    """Add element e to the start of the LinkedList."""
    # to do by Students
    a = Node(e)
    a._next = self._head
    self._head = a
    self._size+=1


    
  def deleteFirst(self):
    """Remove and return the first element from the LinkedList.

    Raise Empty exception if the Linked list is empty.
    """
    if self.is_empty():
      raise Empty('LinkedList is empty')
    # to do by Students
    else:
      a = self._head._element
      self._head = self._head._next
      self._size -= 1
    return a


  def unOrderedSearch(self,target):
    # Search for the target element in the Linked List
    # to do by Students
    current = self._head
    while current != None and current != target:
      current = current._next
    if current != None:
      return current._element
    else:
      return "Not Found"


  def printAll(self):
      # print the contents of the Linked List
      # to do
      result =""
      currNode = self._head
      while currNode is not None:
          result += str(currNode._element)+" "
          currNode = currNode._next
    
      return result[:-1]
  
linkedlist1 = Single_Linked_List()
linkedlist1.insertAtFirst(5)
linkedlist1.insertAtFirst(10)
linkedlist1.insertAtFirst(22)
linkedlist1.insertAtFirst(35)

print("LinkedList contents: "+linkedlist1.printAll()) #35 22 10 5

print(linkedlist1.deleteFirst()) #35
print(linkedlist1.deleteFirst()) #22
print("LinkedList contents: "+linkedlist1.printAll()) #10 5

print(linkedlist1.unOrderedSearch(20)) #Not found
print("LinkedList contents: "+linkedlist1.printAll()) #10 5
