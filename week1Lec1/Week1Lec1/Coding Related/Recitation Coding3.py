def isFunny(num):
    if num <= 0:
        return False
    if num == 1:
        return True

    while num>=2 and (num % 2 == 0 or num % 3 == 0 or num % 5 == 0):
        if num % 2 == 0:
            num = num/2
        elif num % 3 == 0:
            num = num/3
        elif num % 5 == 0:
            num = num/5

    result = num==1
    return result

print(isFunny(13))
