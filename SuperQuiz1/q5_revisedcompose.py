def revisedcompose (hdrlen, tosdscp, identification, flags, fragmentoffset, timetolive, protocoltype, sourceaddress, destinationaddress, payload):
    
    if hdrlen >= 2**4 or hdrlen < 5:
        return 2
    if tosdscp >= 2**6 or tosdscp < 0:
        return 3
    if identification >= 2**16 or identification < 0:
        return 5
    if flags >= 2**3 or flags < 0:
        return 6
    if fragmentoffset >= 2**13 or fragmentoffset < 0:
        return 7
    if timetolive >= 2**8 or timetolive < 0:
        return 8
    if protocoltype >= 2**8 or protocoltype < 0:
        return 9
    if sourceaddress >= 2**32 or sourceaddress < 0:
        return 11
    if destinationaddress >= 2**32 or destinationaddress < 0:
        return 12
    
    version = 4
    totallength = (hdrlen * 4) + len(payload)
    hdr = bytearray(hdrlen * 4)
    
    hdr[0] = (version << 4)
    hdr[0] = (hdr[0] | hdrlen)
    hdr[1] = tosdscp << 2 
    hdr[2] = totallength >> 8
    hdr[3] = (totallength & 0x00FF)
    hdr[4] = identification >> 8
    hdr[5] = identification & 0x00FF
    hdr[6] = flags << 5
    hdr[6] = fragmentoffset >> 8
    hdr[7] = fragmentoffset & 0x00FF
    hdr[8] = timetolive
    hdr[9] = protocoltype
    hdr[12] = sourceaddress >> 24
    hdr[13] = (sourceaddress & 0x00FF0000) >> 16
    hdr[14] = (sourceaddress & 0x0000FF00) >> 8
    hdr[15] = (sourceaddress & 0x0000000FF)
    hdr[16] = destinationaddress >> 24
    hdr[17] = (destinationaddress & 0x00FF0000) >> 16
    hdr[18] = (destinationaddress & 0x0000FF00) >> 8
    hdr[19] = (destinationaddress & 0x0000000FF)
    
    N = len(hdr)  
    hdrchecksum = 0
    for i in range(N):
        hdrchecksum += hdr[i]*2**(i*8)

    while hdrchecksum > 0xFFFF:
        hdrchecksum0 = hdrchecksum & 0xFFFF
        hdrchecksum1 = hdrchecksum >> 16
        hdrchecksum = hdrchecksum0 + hdrchecksum1
    
    hdrchecksum = hdrchecksum^0xFFFF
    
    hdr[11] = hdrchecksum >> 8
    hdr[10] = hdrchecksum & 0x00FF
    for i in range(len(payload)):
        hdr.append(payload[i])
    
    return hdr

print(revisedcompose (6, 24, 4711, 0, 22, 64, 0x06, 0x22334455, 0x66778899, bytearray([0x10, 0x11, 0x12, 0x13, 0x14, 0x15])))