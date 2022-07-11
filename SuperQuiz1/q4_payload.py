def payload (pkt):
    
    hdrlen = pkt[0] & 0x0f
    num = (hdrlen * 32) // 8
    
    return pkt[num:]

print(payload(bytearray(b'E\x00\x00\x17\x00\x00\x00\x00@\x06i\x8d\x11"3DUfw\x88\x10\x11\x12')))