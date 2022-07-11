"""
Consider p-persistent CSMA with a probability value 0 < p < 1. Suppose an idle station gets a new packet to transmit, the medium is completely idle and no other station has a packet. Please find an expression for the average access delay (as a number of minislots) and implement it as a Python function.
"""
def p_persistent_csma_access_delay (p):
    return (1-p)/p

print ("{:.3f}".format(p_persistent_csma_access_delay(0.1)))
