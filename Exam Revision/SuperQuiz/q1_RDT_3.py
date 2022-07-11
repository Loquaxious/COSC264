"""
Sender side simulation of RDT 3.0;

Input packets are formatted
[type, seq_num, message]
0 message with seq_num to be sent;
1 ACK received; acking seq_num;
2 timeout event; resend last packet; 

Output packets are formatted
[status, seq_num]
-1 unexpected packet, -1 as seq_num;
0 message sent successfully, seq_num is the seq # of the message;
1 ACK processed; seq_num is the ACk seq_num;
2 resending finished; seq_num is the seq_num of the resent message;

Four states as described in the FSM
0 - wait for data 0;
1 - wait for ack 0;
2 - wait for data 1;
3 - wait for ack 1;

"""

def RDT_sender(event,state):        
    #Adding your own code below
    if state == 0: #initial state; only accepts data 0; return error otherwise;
        if event[0] == 0 and event[1] == 0:
            return (1, [event[0],event[1]])
        else:
            return (0, [-1,-1])
    
    if state == 1:
        if event[0] == 1:
            if event[1] == 0:
                return (2, [event[0], event[1]])
            else:
                return (1, [-1, -1])
        elif event[0] == 2:
            return (1, [2, 0])
        else:
            return (1, [-1, -1])        
    
    if state == 2:
        if event[0] == 0 and event[1] == 1:
            return (3, [event[0],event[1]])
        else:
            return (2, [-1,-1])        
    
    if state == 3:
        if event[0] == 1:
            if event[1] == 1:
                return (0, [event[0], event[1]])
            else:
                return (3, [-1, -1])
        elif event[0] == 2:
            return (3, [2, 1])
        else:
            return (1, [-1, -1])         


       

#Do not modify the following lines    
def sndr_test(event_list):    
    state = 0
    action_list = []    
    
    for event in event_list:        
        state, action = RDT_sender(event,state)
        action_list.append(action)    
    print(f'{action_list}')

if __name__ == '__main__':
    sndr_test([[0, 0, 1], [2, 0, 1]]) 
    sndr_test([[0, 0, 1], [1, 0, 1], [0, 1, 3], [2],[1,1,3]])
    sndr_test([[0, 0, 1], [0, 1, 2], [0, 0, 3], [0, 1, 4], [0, 0, 5]])    
    sndr_test([[0, 0, 1], [1, 0, 1], [0, 1, 3], [1, 1, 3], [0, 1, 4]])    