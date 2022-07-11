def encodedate (day, month, year):
    if (month > 12 or month < 1) or (day > 31 or day < 1) or  \
       (year < 1 or year > 8388607):
        return -1
    else:
        x = (month - 1) << 28 
        x = (x & 0xF07FFFFF) | (day - 1) << 23
        x = (x & 0xFF800000) | year
        
        return x



print(encodedate(5,5,2017))
print(encodedate(9,11,4444))
print(encodedate(30,12,345752))
print(encodedate(32,5,2017))
print(encodedate(5,15,2017))
print(encodedate(0,5,2017))
print(encodedate(5,0,2017))