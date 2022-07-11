"""
Suppose the data rate is given by R bps and we are given a packet of length L bytes. How long does the transmission of this packet take (i.e. how much time passes between the start of the first bit and the end of the last bit of this packet)? Fill in the following Python3 function with the correct expression. The result needs to be returned in units of seconds.
"""
def transmission_delay (packetLength_bytes, rate_bps):
    return (packetLength_bytes * 8) / rate_bps

print ("{:.3f}".format(transmission_delay(1000000, 4000000)))