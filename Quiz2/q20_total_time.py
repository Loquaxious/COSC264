def total_time (cableLength_KM, packetLength_b):
    propigation_delay = cableLength_KM / 200000
    transmission_delay = packetLength_b / (10*(10**9))
    milli_result = (propigation_delay + transmission_delay) * 1000
    return milli_result

print ("{:.4f}".format(total_time(10000, 8000)))