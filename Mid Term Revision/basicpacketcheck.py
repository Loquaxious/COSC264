def basicpacketcheck (pkt):
    if len(pkt) < 20:
        return 1
    if pkt[0] >> 4 != 4:
        return 2
    
    X = sum(pkt[i]*2**(i*8) for i in range(20)) 
    while X > 0xFFFF:
        X0 = X & 0xFFFF
        X1 = X >> 16
        X = X0 + X1
    if X != 0xFFFF:
        return 3
    
    if pkt[2]*2**8 + pkt[3] != len(pkt):
        return 4
    
    return True
    
pkt1 = bytearray ([0x45, 0x0, 0x0, 0x1e, 0x4, 0xd2, 0x0, 0x0, 0x40, 0x6, 0x20, 0xb4, 0x12, 0x34, 0x56, 0x78, 0x98, 0x76, 0x54, 0x32, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])
print(basicpacketcheck(pkt1))
pkt2 = bytearray ([0x45, 0x0, 0x0, 0x1e, 0x16, 0x2e, 0x0, 0x0, 0x40, 0x6, 0xcd, 0x59, 0x66, 0x66, 0x44, 0x44, 0x98, 0x76, 0x54, 0x32, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])
print(basicpacketcheck(pkt2))
pkt3 = bytearray ([0x45, 0x0, 0x0, 0x1b, 0x12, 0x67, 0x20, 0xe, 0x20, 0x6, 0x35, 0x58, 0x66, 0x66, 0x44, 0x44, 0x55, 0x44, 0x33, 0x22, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0])
print(basicpacketcheck(pkt3))