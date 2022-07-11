"""
The intermediate router B can only start to process a packet (e.g. checking its checksum, figuring out the next hop) once it has completely received the packet. The actual processing time of a router is P seconds. The receiving node C also needs to spend processing time P on the packet. Suppose station A starts to send a packet with S user data bits and O overhead bits to station C. Find a general expression for the time between A starting the transmission of this packet and C having processed the received packet, depending on L (the length of a link in km), C (speed of light in km/s), P (processing delay in B and C in seconds), R (data rate in bps) and O and S. We call this time the packet transfer time. Please implement your expression as a Python function.
"""
def packet_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b):
    L = linkLength_km
    C = speedOfLight_kms
    P = processingDelay_s
    R = dataRate_bps
    S = maxUserDataBitsPerPacket_b
    O = overheadBitsPerPacket_b
    pkt_size = S + O
    prop = L / C
    trans = pkt_size / dataRate_bps
    return (prop + trans + processingDelay_s) * 2

print ("{:.4f}".format(packet_transfer_time(10000, 200000, 0.001, 1000000, 1000, 100)))
print(packet_transfer_time (15000, 250000, 0.001, 1000000, 4192, 100))