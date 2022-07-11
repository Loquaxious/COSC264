"""
Now suppose that A has a message of size M bits which is an integer multiple of the maximum packet user data size of S bits. Station A prepares M/S packets and sends them back-to-back, without any gap. Nodes B and C can also process incoming packets without a gap: if a node has finished processing one packet (which takes P seconds processing time) and the next packet has been completely received at this time, processing of this next packet can start immediately and we have a kind of "pipelining effect". With this, and re-using the general expression for the time by which C will have processed the first packet, find a general expression for the time by which C will have processed all M/S packets (use the simplification that M/S is an integer and there are hence no slack packets). Implement your expression as a Python function.

Note that station B can process incoming packets and transmit outgoing packets at the same time.
"""
def total_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    l = linkLength_km
    c = speedOfLight_kms
    p = processingDelay_s
    r = dataRate_bps
    s = maxUserDataBitsPerPacket_b
    o = overheadBitsPerPacket_b
    m = messageLength_b
    n_pkts = m / s
    pkt_len = s + o
    prop = l / c
    trans = pkt_len / r
    first_pkt_tt = (prop + trans + processingDelay_s)*2
    pkt_tt = trans * (n_pkts -1)
    return first_pkt_tt + pkt_tt

print ("{:.4f}".format(total_transfer_time(20000, 200000, 0.001, 1000000, 1000, 100, 5000)))
print(total_transfer_time (10000, 200000, 0.001, 1000000, 1000, 100, 1000000000))