def pascal(n):
    """
    :param n: Int -- Levels of pascal triangle

    :return: List[List[Int]] -- a list of sublists, which contains pascal values.
    """
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = pascal(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result

def main():
    print(pascal(4))    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

if __name__ == '__main__':
    main()




