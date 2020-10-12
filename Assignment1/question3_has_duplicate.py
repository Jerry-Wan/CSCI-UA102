def has_duplicate(list1):
    """
    remember to mention your runtime as comment!

    :param l: List -- list of integers
    :return: True if list1 has duplicate, return False otherwise.
    """
    list2 = []
    for a in list1:
        if a in list2:
            return True
        else:
            list2.append(a)
    return False
#The big O complexity of the program is O(N)

'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print(has_duplicate([0,6,2,4,9]))   # False

    print(has_duplicate([0,6,2,4,9,1,2]))   # True

if __name__ == '__main__':
    main()
