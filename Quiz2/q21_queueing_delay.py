def queueing_delay (rate_bps, numPackets, packetLength_b):
    return packetLength_b / rate_bps * numPackets

print ("{:.3f}".format(queueing_delay(1000000, 7, 10000)))
