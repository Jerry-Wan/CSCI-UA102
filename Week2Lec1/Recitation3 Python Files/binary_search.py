import random
def binary_search_rec(x, sorted_list):
    # this function uses binary search to determine whether an ordered array
    # contains a specified value.
    # return True if value x is in the list
    # return False if value x is not in the list
    # If you need, you can use a helper function.
    # TO DO
    high = len(sorted_list)-1
    low = 0
    mid =(low+high)//2

    if low >high:
        return False
    elif low == high:
        return sorted_list[low] == x
    else:
        if sorted_list[mid]<x:
            sorted_list = sorted_list[mid+1:]
            return binary_search_rec(x, sorted_list)
        elif sorted_list[mid]>x:
            sorted_list = sorted_list[:mid-1]
            return binary_search_rec(x, sorted_list)
        else:
            return True      

def binary_search_iter(x, sorted_list):
    # TO DO
    # return True if value x is in the list
    # return False if value x is not in the list
    low = 0
    high = len(sorted_list)-1
    mid = 0

    while low<=high:
        mid = (low+high)//2

        if sorted_list[mid]<x:
            low = mid+1
        elif sorted_list[mid]>x:
            high = mid-1
        else:
            return True
    return False
    
 



def main():
    sorted_list = []
    for i in range(100):
        sorted_list.append(random.randint(0, 100))
    sorted_list.sort()

    print("Testing recursive binary search ...")
    for i in range(5):
        value = random.randint(0, 100)
        answer = binary_search_rec(value, sorted_list)
        if (answer == True):
            print("List contains value", value)
        else:
            print("List does not contain value", value)

    print("Testing iterative binary search ...")
    for i in range(5):
        value = random.randint(0, 100)
        answer = binary_search_iter(value, sorted_list)
        if (answer == True):
            print("List contains value", value)
        else:
            print("List does not contain value", value)
    
main()









