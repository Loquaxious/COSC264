def convert (x, base):
    """Calculates the base reprsentation of x given a base value and a unsigned integer x"""
    
    if not isinstance(x, int):
        return -1
    elif not isinstance(base, int):
        return -2
    elif x < 0:
        return -3
    elif base < 2:
        return -4
    else:
        current = x
        result = []
        count = 0
        while current != 0:
            result.append(current % base)
            current //= base
    result.reverse()
    return result

print (convert(1234, 10))
print (convert(4660, 16))