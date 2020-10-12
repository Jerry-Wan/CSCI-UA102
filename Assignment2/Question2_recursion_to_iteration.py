def recur(n):
    if (n < 0):
        return -1
    elif (n < 10):
        return 1
    else:
        return 1 + recur(n // 10)

def iterative(n):
    """
    Implement this function. This function should do exactly the same job as recur(n).
    """
    if n <0:
        return -1
    else:
        result=0
        while n>0:
            if n<10:
                result+=1
                break
            else:
                result +=1
                n = n//10
        return result

def main():
    print(recur(21512))
    print(recur(9891287412))
    print(recur(-9891287412))
    print(iterative(21512))
    print(iterative(9891287412))
    print(iterative(-9891287412))

if __name__ == '__main__':
    main()
