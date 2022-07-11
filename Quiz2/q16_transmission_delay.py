def transmission_delay (packetLength_bytes, rate_mbps):
    return (packetLength_bytes*8) / (rate_mbps*(10**6)) 

print ("{:.3f}".format(transmission_delay(1000000, 4)))
