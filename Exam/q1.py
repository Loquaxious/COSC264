def EstimatedRTT(sampleRTT):
    alpha = 0.125
    estRTT = float(sampleRTT[0])
    for time in sampleRTT:
        estRTT = (1 - alpha) * estRTT + (alpha*float(time))
    
    return estRTT
    
    
print ("{:.3f}".format(EstimatedRTT([1])))
print ("{:.3f}".format(EstimatedRTT([1,2])))
print ("{:.3f}".format(EstimatedRTT([1,2,3])))
