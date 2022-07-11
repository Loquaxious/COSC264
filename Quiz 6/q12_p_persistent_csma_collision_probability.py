"""
Consider the same setting as in the previous question, but now with p-persistent CSMA for some probability value 0 < p < 1. Please find an expression for the probability that both contenders collide. Assume that they are statistically independent. You will need to:

work out the probability that they collide in the first time slot, the probability that they collide in the second time slot, the probability that they collide in the k-th time slot etc.,
combine these probabilities using the law of total probability,
and when calculating the end result you will need the sum formula for the (infinite) geometric series.
Implement your expression as a Python function.
"""
def p_persistent_csma_collision_probability (p): 
    q = 1-p
    return p**2/(1-(q**2))

print ("{:.3f}".format(p_persistent_csma_collision_probability(0.2)))
