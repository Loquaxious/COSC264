"""
Same setup as in the previous question. If we call your result from the previous question P, then P can be interpreted as the packet error probability or packet loss probability (or more precisely: the probability that at least one bit in the packet is incorrect). Suppose a transmitter wants to transmit a packet with L bits to a receiver and carries out retransmissions until successful (the transmitter always receives reliable feedback from the receiver about the transmission outcomes). Find an expression for the average number of transmission trials in terms of the packet length L (in bits) and the bit error probability P and implement it in the Python function below. You will need the result for an earlier question.
"""
def avg_trials_from_ber (bit_error_probability, packetLength_b):
    per = 1-(1-bit_error_probability)**packetLength_b
    return 1/ (1-per)

print ("{:.3f}".format(avg_trials_from_ber(0.0001, 1000)))
print(avg_trials_from_ber(0.005, 1000))
print(avg_trials_from_ber(0.001, 2000))