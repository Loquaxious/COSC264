def total_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    l = linkLength_km
    c = speedOfLight_kms
    p = processingDelay_s
    r = dataRate_bps
    s = maxUserDataBitsPerPacket_b
    o = overheadBitsPerPacket_b
    m = messageLength_b
    
    n_packets = m / s 
    
    prop = l / c
    trans = (s + o) / r
    transfer_time = (prop + (p * n_packets) + trans) * 2
    
    print(n_packets)
    print(prop)
    print(trans)
    
    return transfer_time


print ("{:.4f}".format(total_transfer_time(20000, 200000, 0.001, 1000000, 1000, 100, 5000)))
