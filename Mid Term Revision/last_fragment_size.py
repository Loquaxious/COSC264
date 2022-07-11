"""
Find a general expression for the size of the last fragment which involves only the parameters S, M, and O and possibly one of the functions ceil, floor. Implement it as a Python function.
"""
import math
def last_fragment_size (messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes
    max_data = m - o
    n_pkts = math.floor(s / max_data)
    lst_pkt = s - (n_pkts * max_data)
    return o + lst_pkt

print (last_fragment_size(10000, 100, 1000))