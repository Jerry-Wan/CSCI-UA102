import timeit
import matplotlib.pyplot as plt
import random

def timeFunction(f,n,repeat=1):
    return timeit.timeit(f.__name__+'('+str(n)+')',setup="from __main__ import "+f.__name__,number=repeat)/repeat


def permutation1(N):
    """
    generate a random permutation from 0 to N-1. 

    :param N: Int - The boundary integer.
    :return: List -- A list of integers from 0 to N - 1. Random permutation.
    """
    a = [None]*N
    for b in range(N):
        random_number = random.randint(0,N-1)
        able = True
        for c in range(b):
            if a[c] == random_number:
                able = False
        if able == True:
            a[b] = random_number
    return a
    

    


def permutation2(N):
    """
    generate a random permutation from 0 to N-1. 

    :param N: Int -- The boundary integer.
    :return: List -- A list of integers from 0 to N - 1. Random permutation.
    """
    a = [None]*N
    used = [None]*N
    for b in range(N):
        random_number = random.randint(0,N-1)
        if used[random_number]!= True:
            a[b] = random_number
            used[random_number]= True
    return a

def permutation3(N):
    """
    generate a random permutation from 0 to N-1. 

    :param N: Int -- The boundary integer.
    :return: List -- A list of integers from 0 to N - 1. Random permutation.
    """
    a = [None]*N
    for b in range(N):
        a[b] = b
        a[b],a[random.randint(0,b)] = a[random.randint(0,b)],a[b]
        
        

def plot_data():
    x = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]
    y = []
    z = []
    j = []
    for each in x:
        y.append(timeFunction(permutation1, each))
        z.append(timeFunction(permutation2, each))
        j.append(timeFunction(permutation3, each))
    line1, = plt.plot(x, y, label="permutation1")
    plt.legend()
    line2, = plt.plot(x, z, label="permutation2")
    plt.legend()
    line3, = plt.plot(x, j, label="permutation3")
    plt.legend(handles=[line1,line2,line3])
    plt.xlabel("Input Size")
    plt.ylabel("Run time -- Seconds")
    plt.show()

if __name__ == '__main__':
    plot_data()

        
