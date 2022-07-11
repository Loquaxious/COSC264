def packetSwitching (numberRouters, messageSize_b, userDataSize_b, overheadSize_b, processingTime_s, dataRate_bps, propagationDelay_s):
    N  =  numberRouters
    M  =  messageSize_b
    S  =  userDataSize_b
    O  =  overheadSize_b
    P  =  processingTime_s
    R  =  dataRate_bps
    T  =  propagationDelay_s
    
    n_pkt = M/S
    pkt_s = S + O
    trans = pkt_s / R
    
    print(((P + T + trans) * N+1))
    print((n_pkt -1 * trans))
    print(((P + T + trans) * N+1) + (n_pkt -1 * trans))
    
    return ((P + T + trans) * N+1) + (n_pkt -1 * trans)

print(abs(packetSwitching(3, 10000, 1000, 100, 0.001, 1000000, 0.02)-0.0973)<0.0001)
