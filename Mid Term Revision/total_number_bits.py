"""
Suppose a packet can carry at most S bits of user data and requires O bits of overhead. We are given a message of M bits, and M is not necessarily an integer multiple of S. Please find an expression for the total number of bits (user data and overhead bits) that need to be transmitted to transmit all M user data bits in packets. Please implement your expression as a Python function.

The math Python library provides functions like math.floor or math.ceil that can be used for rounding.
"""
import math
def total_number_bits (maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    S = maxUserDataBitsPerPacket_b
    O = overheadBitsPerPacket_b
    M = messageLength_b
    pkt_size = S + O
    n_pkts = M / S
    if (n_pkts).is_integer():
        return pkt_size * n_pkts
    else:
        n_pkts = math.floor(M / S)
        extra = M - n_pkts * S
        return pkt_size * n_pkts + (extra + O)        


print ("{:.1f}".format(total_number_bits(1000, 100, 10000)))
print ("{:.1f}".format(total_number_bits(1000, 100, 10001)))
print ("{:.1f}".format(total_number_bits(1000, 100, 10999)))
