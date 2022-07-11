def per_from_ber (bitErrorProb, packetLen_b):
    return 1-((1-bitErrorProb)**packetLen_b)

print ("{:.3f}".format(per_from_ber(0.0001, 1000)))
print ("{:.3f}".format(per_from_ber(0.001, 1000)))
print ("{:.5f}".format(per_from_ber(0.01, 1000)))
