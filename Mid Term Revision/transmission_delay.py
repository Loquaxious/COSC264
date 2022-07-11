"""
Please work out a general expression for the total combined transmission delay of all call-setup-request and call-setup-response transmissions and implement it as a Python function.
"""
def transmission_delay (numberSwitches, dataRate_bps, messageLengthRequest_b, messageLengthResponse_b):
    N     = numberSwitches
    R     = dataRate_bps
    Mreq  = messageLengthRequest_b
    Mresp = messageLengthResponse_b
    
    return ((N+1) * (Mreq/R)) + ((N+1) * (Mresp/R))

print (abs(transmission_delay(3, 10000000, 2000, 1000)-0.0012)<0.0001)