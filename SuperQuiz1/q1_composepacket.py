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
    
    array = bytearray(20)
    array[0] = (version << 4)
    array[0] = (array[0] | hdrlen)
    array[1] = tosdscp << 2 
    array[2] = totallength >> 8
    array[3] = (totallength & 0x00FF)
    array[4] = identification >> 8
    array[5] = identification & 0x00FF
    array[6] = flags << 5
    array[6] = fragmentoffset >> 8
    array[7] = fragmentoffset & 0x00FF
    array[8] = timetolive
    array[9] = protocoltype
    array[10] = headerchecksum >> 8
    array[11] = headerchecksum & 0x00FF
    array[12] = sourceaddress >> 24
    array[13] = (sourceaddress & 0x00FF0000) >> 16
    array[14] = (sourceaddress & 0x0000FF00) >> 8
    array[15] = (sourceaddress & 0x0000000FF)
    array[16] = destinationaddress >> 24
    array[17] = (destinationaddress & 0x00FF0000) >> 16
    array[18] = (destinationaddress & 0x0000FF00) >> 8
    array[19] = (destinationaddress & 0x0000000FF)
    
    return array

def main():
    # test1
    print(composepacket(5,5,0,4000,24200,0,63,22,6,4711, 2190815565, 3232270145))
    # test 2
    print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145))
    #test 3
    print(composepacket(4,16,0,4000,24200,0,63,22,6,4711, 2190815565, 3232270145))
    #test 4
    print(composepacket(4,15,64,4000,24200,0,63,22,6,4711, 2190815565, 3232270145))
    #test5
    print(composepacket(4,-3,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145))
    #test6
    print(composepacket(4,5,0,1500,-24200,0,63,22,6,4711, 2190815565, 3232270145))
    #test7
    print(composepacket(4,5,0,1500,24200,0,63,22,6,-4711, 2190815565, 3232270145))    
    
    
if __name__ == "__main__":
    main()