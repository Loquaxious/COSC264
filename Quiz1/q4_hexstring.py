def hexstring (x):
    """Uses convert() from q3 to convert a unsinged integer to a hexstring""" 
    if not isinstance(x, int):
        return -1
    elif x < 0:
        return -2
    else:
        chars = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
        decimals = convert(x, 16)
        result = ''
        for num in decimals:
            if num >= 10:
                result += chars[num]
            else:
                result += str(num)
        return '0x' + result


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


print(hexstring(1234))