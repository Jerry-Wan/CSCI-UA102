class Empty(Exception):
    ''' Raise this class for exceptions '''
    pass

class ArrayStack:
    ''' Stack implemented with python list append/pop'''
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def is_empty(self):
        return len(self.array) == 0

    def push(self, e):
        self.array.append(e)

    def top(self):
        if self.is_empty():
            raise Empty()
        return self.array[-1]

    def pop(self):
        if self.is_empty():
            raise Empty()
        return self.array.pop(-1)

    def __repr__(self):
            return str(self.array)
        
def spans1(X):
    '''
    :param X: List[Int] -- list of integers.

    No stack allowed. For each index, 
    we look to the front of array until we find a value that is greater.

    @return: list of span values.
    '''
    pass
        



def spans2(X):
    '''
    :param X: List[Int] -- list of integers.

    Use a stack. We use the stack to compute the span distance.

    If the top of the stack is “Smaller” than the next data, 
    top of the stack should be popped.

    :return: list of span values.
    '''
    pass


def main():
    print(spans1([6,3,4,5,2])) # [1, 1, 2, 3, 1]
    print(spans1([6,7,1,3,4,5,2]))  # [1, 2, 1, 2, 3, 4, 1]
    print(spans2([6,3,4,5,2])) # [1, 1, 2, 3, 1]
    print(spans2([6,7,1,3,4,5,2]))  # [1, 2, 1, 2, 3, 4, 1]

if __name__ == '__main__':
    main()

 



        
