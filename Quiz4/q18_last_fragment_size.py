import math
def last_fragment_size (messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes
    
    n_data = m - o
    total_ndata = n_data * math.floor(s/n_data)   
    
    return (s - total_ndata) + o

print (last_fragment_size(10000, 100, 1000))
	
print (last_fragment_size(13545, 120, 1500))

print (last_fragment_size(17755, 180, 1500))

print (last_fragment_size(1500, 20, 1500))