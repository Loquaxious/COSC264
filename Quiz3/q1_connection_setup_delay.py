def connection_setup_delay (cableLength_km, speedOfLight_kms, dataRate_bps, messageLength_b, processingTimes_s):
    prop = cableLength_km / speedOfLight_kms
    trans = messageLength_b / dataRate_bps
    result = (prop*4 + trans*4) + processingTimes_s*4 
    return result

print ("{:.4f}".format(connection_setup_delay(10000, 200000, 1000000, 1000, 0.001)))
