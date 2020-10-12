import random

def quick_select(array, k):
    """ Return the kth smallest element of array, for k from 1 to len(array).
        :param array: List[Int] -- select kth smallest element from it.
        :param k:     Int -- kth smallest, ranging from 1 to len(array)

        return: value of kth smallest element within a rray
    """
    '''
    # To do
    for a in range(2,len(array)):
        for j in range(0,len(array)-2):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array[k-1]
    '''
    if len(array) == 1:
        return array[0]
    pivot = random.choice(array)
    less = [x for x in array if x < pivot]
    equal = [y for y in array if y == pivot]
    greater = [z for z in array if z > pivot]
    if k <= len(less):
        return quick_select(less, k)
    elif k <= len(less + equal):
        return pivot
    else:
        j = k - (len(less) + len(equal))
        return quick_select(greater, j)
                           


def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))
    print(array)
    k = random.randint(1,20)
    print("Selecting:", k,"th element......")
    print("Your result is:", quick_select(array, k))
    array.sort()
    print("Correct result should be:", array[k - 1])

if __name__ == '__main__':
    main()
