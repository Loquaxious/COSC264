"""
Suppose we have a transmitter and a receiver which communicate over a channel that loses packets with a fixed packet loss probability P in (0,1). The transmitter wants to transmit one packet to the receiver and after each packet transmission trial the transmitter gets correct feedback on whether or not the transmission was successful. If the transmission failed, the transmitter performs a re-transmission, and it repeats this until the transmission is successful.
What is the average number of packet transmission trials that the transmitter has to make when the packet loss probability is P in (0,1)? Please find an expression and fill it into the Python function below.
"""
def average_trials (P):
    return 1/(1-P)

print ("{:.3f}".format(average_trials(0.1)))