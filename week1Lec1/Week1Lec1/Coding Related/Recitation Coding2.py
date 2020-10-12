def mostNumber(s):
    dic1 = {}
    for a in s:
        if a in dic1:
            dic1[a]=dic1[a]+1
            if dic1[a]>= len(s)/2:
                break
        else:
            dic1[a] = 1
    return a

x = [1,1,1,3,3,3,3]
print(mostNumber(x))
