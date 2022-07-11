def packet_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b):
    L = linkLength_km
    C = speedOfLight_kms
    P = processingDelay_s
    R = dataRate_bps
    S = maxUserDataBitsPerPacket_b
    O = overheadBitsPerPacket_b
    
    prop = L / C
    trans = (S + O) / R
    return (prop + P + trans)*2

print ("{:.4f}".format(packet_transfer_time(10000, 200000, 0.001, 1000000, 1000, 100)))
print ("{:.6f}".format(packet_transfer_time(15000, 250000, 0.001, 1000000, 4192, 100)))
