def queueingDelay (packetSize_bits, dataRate_bps, flagCurrentTransmission, numberInQueue):
    L    =  packetSize_bits
    R    =  dataRate_bps
    flag =  flagCurrentTransmission
    N    =  numberInQueue
    
    trans = L/R
    if flag:
        print((N * trans) + trans)
        return (N * trans) + trans
    else:
        return N * trans
    return

print(abs(queueingDelay(1000,1000000,True,0)-0.0005)<0.00001)
print(abs(queueingDelay(1000,1000000,False,0)-0.0000)<0.00001)