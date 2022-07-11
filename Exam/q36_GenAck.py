def GenACK(segments):
    segSize = 100
    ack = [segments[0] + segSize]
    cur_seg = ack[0]
    for i in range(1, len(segments)):
        if segments[i] == cur_seg:
            ack.append(segments[i] + segSize)
            cur_seg = ack[i]
        else:
            ack.append(cur_seg)
    return ack

print(GenACK([1,101,201]))
print(GenACK([1]))
print(GenACK([1,101]))
print(GenACK([1,201,301]))
print(GenACK([1,201,101]))
print(GenACK([1,201,101,101]))
print(GenACK([1,1]))
