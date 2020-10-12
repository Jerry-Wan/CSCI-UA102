    
def inplace_quick_sort(S, a, b,count = 0):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""

    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
    if a >= b: 
        return    
    middle = (a + b) // 2 
    if S[a] > S[middle]:             #Swap three points and make it left < middle < right
        S[a], S[middle] = S[middle], S[a] 
    if S[b] < S[middle]: 
        S[b], S[middle], = S[middle], S[b] 
    if S[a] > S[middle]: 
        S[a], S[middle] = S[middle], S[a] 
    pivot = S[middle] 
    S[b], S[middle] = S[middle], S[b]                   #Put the pivot the last element 
    left = a                                               # will scan rightward
    right = b - 1                                            # will scan leftward
    
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:                                    # scans did not strictly cross
            S[left], S[right] = S[right], S[left]              # swap values
            left, right = left + 1, right - 1                  # shrink range
            
    # put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left + 1, b)
    

def main():
    import random
    S = []
    for i in range(1000):
        S.append(random.randint(-10000, 10000))

    print(S)
    inplace_quick_sort(S, 0, len(S) - 1)
    print(S)
    print("Is S sorted???", S == sorted(S))
    
if __name__ == '__main__':
    main()
