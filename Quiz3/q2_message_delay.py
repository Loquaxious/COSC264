def message_delay (connSetupTime_s, cableLength_km, speedOfLight_kms, messageLength_b, dataRate_bps):
    prop = cableLength_km / speedOfLight_kms
    trans = messageLength_b / dataRate_bps
    return connSetupTime_s + prop*2 + trans

print ("{:.3f}".format(message_delay(0.305, 15000, 200000, 5000, 1000000)))
