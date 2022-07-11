"""
Suppose we have an overall system bandwidth of B Hz. The bandwidth required for a guard band is G Hz and the bandwidth required for one user channel (sub-channel) is U Hz. Please find an expression for the maximum number N of users that can be accommodated in the system and implement it as a Python function. You will need one of the functions floor / ceil. Note that there also have to be guard bands above the user on the highest channel and below the user on the lowest channel. In other words, N users require N+1 guard bands.
"""
import math
def number_fdma_channels (b_hz, g_hz, u_hz):
    return math.floor((b_hz - g_hz)/(g_hz + u_hz))

print (number_fdma_channels(1000000, 200, 20000))
