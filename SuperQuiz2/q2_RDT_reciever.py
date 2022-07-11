def RDT_Receiver(packet):
    #Your code here:
    if packet[0] != 0 and packet[0] != 1:
        return [-1, -1]
    else:
        return [0, packet[0]]

#Do NOT modify the following lines    
def rcvr_test(packet_list):    
    action_list = []    
    
    for packet in packet_list:        
        action = RDT_Receiver(packet)
        action_list.append(action)    
        
    print(f'{action_list}')  
    
rcvr_test([[0, 1]])
rcvr_test([[-1, 1]])
rcvr_test([[2, 1]])
rcvr_test([[0, 1], [0, 2]])
rcvr_test([[0, 1], [1, 2]])