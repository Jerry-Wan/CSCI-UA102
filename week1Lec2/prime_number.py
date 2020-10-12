import math
def is_prime1(N):  
    """ 
    Divide N by every number from 2 to N - 1, 
    if it is not divisible by any of them hence it is a prime.

    :param N: Int -- The number being checked.
    :return: True if N is a prime number, return False otherwise.
    """
    for a in range(2,N-1):
        if N%a ==0:
            return False
    return True

def is_prime2(N): 
    """
    Instead of checking until N, we can check until sqrt(N)
    because a larger factor of N must be a multiple of smaller factor that has been already checked.
    
    :param N: Int -- The number being checked.
    :return: True if N is a prime number, return False otherwise.
    """
    a=math.sqrt(N)
    for b in range(2,a):
        if N%a ==0:
            return False
    return True



def main():
    print(is_prime1(1299827))
    print(is_prime1(1296041))# IDK why it turns out to be True but still print the error message
    if not is_prime1(1299827) == True:
        print('1299827 should be a prime but you returned False.')
    if not is_prime1(1296041) == True:
        print('1296041 should be a prime but you returned False.')
    if is_prime1(1296042) == True:
        print('1296042 should not be a prime but you returned True.')

    if not is_prime2(1299827) == True:
        print('1299827 should be a prime but you returned False.')
    if not is_prime2(1296041) == True:
        print('1296041 should be a prime but you returned False.')
    if is_prime2(1296042) == True:
        print('1296042 should not be a prime but you returned True.')



if __name__ == '__main__':
    main()
