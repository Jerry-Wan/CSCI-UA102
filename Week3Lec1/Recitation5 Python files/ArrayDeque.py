 from queue import Empty
class ArrayDeque:
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == ArrayDeque.DEFAULT_CAPACITY

    def first(self):
        return self._data[self._front]

    def last(self):
        return self._data[(self._front+ArrayDeque.DEFAULT_CAPACITY-1)%ArrayDeque.DEFAULT_CAPACITY]

    def delete_first(self):
        if self.is_empty:
            return "Sorry, the list is empty."
        else:
            a = self.first
            self.first = None
            self._front +=1
            self.size -= 1
            return a 

    def add_first(self, e):
        if self.is_full:
            return "Sorry,the list is full"
        else:
            self._data.append(e)
            self._front = (self._front+1) % self._size

    def delete_last(self):
        if self.is_empty:
            return "Sorry, the list is empty."
        else:
            a = self.last
            self.last = None
            self.size -= 1
            return a 


    def add_last(self, e):
        self._data[len(self)-1] = e

    def __str__(self):
        return str(self._data)

def main():
    '''
    # Empty Queue, size 10.
    deque = ArrayDeque()

    # Add 0, 1, 2, 3 following FIFO.
    for i in range(4):
        deque.add_first(i)
    print(deque)  # [None, None, None, None, None, None, 3, 2, 1, 0]

    # Add 4, 5, 6, 7 following LIFO.
    for j in range(4):
        deque.add_last(j + 4)
    print(deque)  # [4, 5, 6, 7, None, None, 3, 2, 1, 0]

    # Remove first one
    print(deque.delete_first()) # 3

    # Remove last one
    print(deque.delete_last()) # 7
    '''
    deque = ArrayDeque()
    for i in range(4):
        deque.add_first(i)
    for j in range(4):
        deque.add_last(j + 4)
    print(deque.delete_first())
    print(deque.delete_last())

if __name__ == '__main__':
    main()
