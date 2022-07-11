import math
def number_fragments (messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes
    
    n_data = m - o
    return math.ceil(s/n_data)

print (number_fragments(10000, 100, 1000))

print (number_fragments(10000, 20, 1500))