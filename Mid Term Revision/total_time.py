"""
We are given a communication cable of length K kilometers, and the speed of light on this cable is 200,000 km/s. We can transmit at a data rate of 10 Gbps and we are given a packet of length L bits. Please complete the Python function below to calculate the total time between the instant where the transmitter starts with transmitting the first bit and the instant where the receiver has just completed the reception of the last bit. The time should be expressed in milliseconds.
"""
def total_time (cableLength_KM, packetLength_b):
    prop = cableLength_KM / 200000
    trans = packetLength_b / (10 * 10**9)
    return (prop + trans)*1000

print ("{:.4f}".format(total_time(10000, 8000)))