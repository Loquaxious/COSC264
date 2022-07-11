"""
Once the call has been established (i.e. we have completed the connection setup phase), any data signal sent by A will be forwarded by B without any additional delay, i.e. during the data forwarding phase (or connection usage phase) things appear as if B is not present at all. If we call the duration of the connection setup phase TS, and we want to transmit a message of length M bits, find a general expression for the total time that passes between A starting the connection setup and C receiving the last bit of the message, assuming that A commences with data transfer immediately after it has received and processed the call-setup-response message. We call this the message delay. Please implement your general expression as a Python function.
"""
def message_delay (connSetupTime_s, cableLength_km, speedOfLight_kms, messageLength_b, dataRate_bps):
    prop = cableLength_km / speedOfLight_kms
    trans = messageLength_b / dataRate_bps
    return connSetupTime_s + (prop)*2 + trans

print ("{:.3f}".format(message_delay(0.305, 15000, 200000, 5000, 1000000)))
print(message_delay(0.2, 10000, 200000, 1000000000, 1*10**6))