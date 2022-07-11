import math
def total_number_bits (maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    S = maxUserDataBitsPerPacket_b
    O = overheadBitsPerPacket_b
    M = messageLength_b
    times = M / S
    if (times).is_integer():
        return (S + O) * times
    else:   
        floor = math.floor(times)
        diff = M - floor * S
        result = (S + O) * floor + (diff + O)
        return result

print ("{:.1f}".format(total_number_bits(1000, 100, 10000)))
print ("{:.1f}".format(total_number_bits(1000, 100, 10001)))
print ("{:.1f}".format(total_number_bits(1000, 100, 10999)))