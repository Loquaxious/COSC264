def avg_trials_from_ber (bit_error_probability, packetLength_b):
    per = 1-((1-bit_error_probability)**packetLength_b)
    return 1/(1-per)

print ("{:.3f}".format(avg_trials_from_ber(0.0001, 1000)))
print ("{:.2f}".format(avg_trials_from_ber(0.005, 1000)))