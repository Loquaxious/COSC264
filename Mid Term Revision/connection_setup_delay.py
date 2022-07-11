"""
Now combine your expressions from the previous problems to find a general expression for the call-setup delay (i.e. the time between A starting to transmit the call-setup-request message and A finishing receiving and processing the call-setup-response message) and implement it as a Python function.
"""
def connection_setup_delay (numberSwitches, cableLength_km, speedOfLight_kms, dataRate_bps, messageLengthRequest_b, messageLengthResponse_b, processingTimes_s):
    N     = numberSwitches
    L     = cableLength_km
    C     = speedOfLight_kms
    R     = dataRate_bps
    Mreq  = messageLengthRequest_b
    Mresp = messageLengthResponse_b
    P     = processingTimes_s
    
    prop = ((N+1) * L / C)*2
    tran = ((N+1) * (Mreq/R)) + ((N+1) * (Mresp/R))
    proc = ((N+1) * P)*2
    
    return prop + tran + proc

print (abs(connection_setup_delay(3, 7500, 200000, 10000000, 2000, 1000, 0.001)-0.3092)<0.0001)
print(connection_setup_delay(10, 2000, 200000, 10000000, 2000, 1000, 0.001))