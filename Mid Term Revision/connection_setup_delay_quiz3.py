"""
Let L stand for the length of one link in km, c stand for the speed of light on the cable (in km/s), R stand for the data rate available on either of the links (in bps), M stand for the length of the call-setup-* messages (in bits), and P stand for the processing times required by A, B and C (in seconds). Find a general expression for the duration of the connection setup phase (i.e. the time between A starting the process and A being able to commence data transmission) and implement it as a Python function.
"""
def connection_setup_delay (cableLength_km, speedOfLight_kms, dataRate_bps, messageLength_b, processingTimes_s):
    prop = cableLength_km / speedOfLight_kms
    trans = messageLength_b / dataRate_bps
    return (prop + trans + processingTimes_s)*4

print ("{:.4f}".format(connection_setup_delay(10000, 200000, 1000000, 1000, 0.001)))
print(connection_setup_delay(10000, 200000, 1000000, 4000, 0.001))