"""
Suppose we are operating with TDMA using a superframe length of S seconds, a guard time of G seconds, and the length of a user slot is U seconds. Please find an expression for the maximum number of users that the system can support and implement it as a Python function. You will need one of the functions ceil/floor.
"""
import math
def number_tdma_users (s_s, g_s, u_s):
    return math.floor((s_s)/(g_s + u_s))

print (number_tdma_users(1, 0.001, 0.008))
print (number_tdma_users(1.2, 0.002, 0.02))
print (number_tdma_users(0.100, 0.001, 0.005))