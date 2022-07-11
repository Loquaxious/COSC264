"""
Please work out a general expression for the total combined propagation delay that all call-setup-request and call-setup-response messages cause, and implement it as a Python function.
"""
def propagation_delay (numberSwitches, cableLength_km, speedOfLight_kms):
    N     = numberSwitches
    L     = cableLength_km
    C     = speedOfLight_kms
    return ((N+1) * L / C)*2

print(propagation_delay(3, 7500, 200000))
print (abs(propagation_delay(3, 7500, 200000)-0.3)<0.0001)