def twowrongbits (pktLength_b, bitErrorProb):
    L = pktLength_b
    P = bitErrorProb
    return (1-bitErrorProb**2) * ((bitErrorProb)**(pktLength_b - 2)) 

print(twowrongbits(1000, 0.001))
print (abs(twowrongbits(1000, 0.001)-0.2642)<0.0001)
