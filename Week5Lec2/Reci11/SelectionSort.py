import random

def selection_sort(array):
    """ The algorithm proceeds by finding the smallest element in the unsorted sublist, 
        exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), 
        and moving the sublist boundaries one element to the right. 
        :param array: List[Int] -- the python list being sorted
    """
    # Your code
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array

def main():
    array = []
    for i in range(1000):
        array.append(random.randint(-10000, 10000))

    print("Before sorting:")
    #print(array)
    selection_sort(array)
    print("After sorting:")
    print(array)

    print(array == sorted(array))
if __name__ == '__main__':
    main()
