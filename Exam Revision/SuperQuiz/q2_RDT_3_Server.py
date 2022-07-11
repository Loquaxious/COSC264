def RDT_Receiver(packet):
    if packet[0] == 0 or packet[0] == 1:
        return [0, packet[0]]
    else:
        return [-1, -1]
    
       




#Do NOT modify the following lines    
def rcvr_test(packet_list):    
    action_list = []    
    
    for packet in packet_list:        
        action = RDT_Receiver(packet)
        action_list.append(action)    
        
    print(f'{action_list}')  
    
if __name__ == '__main__':
    rcvr_test([[0, 1]])