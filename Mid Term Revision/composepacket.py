def composepacket (version, hdrlen, tosdscp, totallength, identification, flags, fragmentoffset, timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress):
    if version != 4 or version < 0:
        return 1
    if hdrlen >= 2**4 or hdrlen < 0:
        return 2
    if tosdscp >= 2**6 or tosdscp < 0:
        return 3
    if totallength >= 2**16 or totallength < 0:
        return 4
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
    if headerchecksum >= 2**16 or headerchecksum < 0:
        return 10
    if sourceaddress >= 2**32 or sourceaddress < 0:
        return 11
    if destinationaddress >= 2**32 or destinationaddress < 0:
        return 12
    
    
    pkt_hdr = bytearray(20)
    pkt_hdr[0] = version << 4
    pkt_hdr[0] = (pkt_hdr[0] & 0xFF) | hdrlen
    pkt_hdr[1] = tosdscp << 2
    pkt_hdr[2] = totallength >> 8
    pkt_hdr[3] = totallength & 0x00FF 
    pkt_hdr[4] = identification >> 8
    pkt_hdr[5] = identification & 0x00FF
    pkt_hdr[6] = flags << 5
    pkt_hdr[6] = (pkt_hdr[6] & 0xFF) | (fragmentoffset >> 8)
    pkt_hdr[7] = fragmentoffset & 0x0FF
    pkt_hdr[8] = timetolive
    pkt_hdr[9] = protocoltype
    pkt_hdr[10] = headerchecksum >> 8
    pkt_hdr[11] = headerchecksum & 0x00FF
    pkt_hdr[12] = sourceaddress >> 24
    pkt_hdr[13] = (sourceaddress & 0x00FF0000) >> 16
    pkt_hdr[14] = (sourceaddress & 0x0000FF00) >> 8
    pkt_hdr[15] = (sourceaddress & 0x000000FF)
    pkt_hdr[16] = (destinationaddress >> 24)
    pkt_hdr[17] = (destinationaddress & 0x00FF0000) >> 16
    pkt_hdr[18] = (destinationaddress & 0x0000ff00) >> 8
    pkt_hdr[19] = destinationaddress & 0x000000ff
    
    return pkt_hdr

if __name__ == '__main__':
    print(composepacket(5,5,0,4000,24200,0,63,22,6,4711, 2190815565, 3232270145))
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145))
            
    
    print(composepacket(4,-3,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145))    
    