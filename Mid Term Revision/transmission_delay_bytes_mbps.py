"""
A communication system provides a specified data rate R on a given link, which is usually specified in Kbps (kilobit per second), Mbps (Megabit per second), Gbps (Gigabit per second) and so on. For example, modern Ethernet technology comes in versions supporting 40 Gbps or even 100 Gbps.

The transmission delay of a packet of L bits length is defined as the time it takes to transmit the packet over the given channel with the given data rate R.

Suppose the data rate is given by R Mbps and we are given a packet of length L bytes. How long does the transmission of this packet take (i.e. how much time passes between the start of the first bit and the end of the last bit of this packet)? Fill in the following Python3 function with the correct expression. The result needs to be returned in units of seconds.
"""
def transmission_delay (packetLength_bytes, rate_mbps):
    pktlen = packetLength_bytes * 8
    rate = rate_mbps * 10**6
    return pktlen / rate

print ("{:.3f}".format(transmission_delay(1000000, 4)))
print(transmission_delay(1000,10))
print(transmission_delay(1000,10000) * 1000)

