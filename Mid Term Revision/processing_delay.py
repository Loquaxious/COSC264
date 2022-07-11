"""
Please work out a general expression for the combined total processing delay incurred for the processing of all call-setup-request and call-setup-response transmissions, and implement it as a Python function.
"""
def processing_delay (numberSwitches, processingTimes_s):
    N     = numberSwitches
    P     = processingTimes_s
    return ((N+1) * P)*2

print (abs(processing_delay(3, 0.001)-0.008)<0.0001)    