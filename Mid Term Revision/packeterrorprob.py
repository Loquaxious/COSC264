def packeterrorprobability (pktLength_b, bitErrorProb):
    L = pktLength_b
    P = bitErrorProb
    return 1-((1-bitErrorProb)**pktLength_b)

print (abs(packeterrorprobability(1000, 0.001)-0.6323)<0.0001)
print(packeterrorprobability(2000,0.0001))