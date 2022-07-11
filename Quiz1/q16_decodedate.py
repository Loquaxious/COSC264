def decodedate (x):
    month = (x & 0xF0000000) >> 28
    day = (x & 0x0F800000) >> 23
    year =  (x & 0x007FFFFF)
    
    return str(day + 1) + '.' + str(month + 1) + '.' + str(year)
    
print(decodedate(1107298273))
print(decodedate(2298488591))
print(decodedate(998246312))