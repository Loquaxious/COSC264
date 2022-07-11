import socket
from datetime import datetime

HOST = '127.0.0.1'
port = None

def is_int(s):
    try:
        int(s) 
        return True
    except ValueError as er:
        print('Value entered should be an integer')
        return False
    
def fileresponse(connection, status, dataLen=None, fileData=None):
    rspnse = bytearray(8)
    rspnse[0] = 0x49
    rspnse[1] = 0x7E
    rspnse[2] = 0x02
    rspnse[3] = status
    if status == 0:
        rspnse[4] = 0x00
        rspnse[5] = 0x00
        rspnse[6] = 0x00
        rspnse[7] = 0x00
    else:
        rspnse[4] = dataLen >> 24
        rspnse[5] = (dataLen & 0x00FF0000) >> 16
        rspnse[6] = (dataLen & 0x0000FF00) >> 8
        rspnse[7] = (dataLen & 0x0000000FF)
        
        for i in range(dataLen):
            rspnse.append(fileData[i])
            
    connection.sendall(rspnse)
  
        
port = input("Enter port: ")
if is_int(port):
    port = int(port)
    if port < 1024 or port > 64000:
        print('Integer should be between 1024 and 64000')
        print('Quitting...')
        quit()
        
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    s.bind((HOST, port))
except socket.error as e:
    print(e)
    print('Quitting...')
    s.close()
    quit()
except socket.timeout:
    print('Socket creation or bind time out')
    print('Quitting...')
    s.close()
    quit()    

try:
    s.listen()
except socket.error:
    print('Connection request error')
    print('Quitting...')
    s.close()
    quit()

while True:
    try:
        conn, addr = s.accept()
        conn.settimeout(1)
        time = datetime.now().strftime("%H:%M:%S")
        print()
        print('Connected to {}, port {} at {}'.format(addr[0], addr[1], time))
        print()
    except socket.timeout:
        continue
    
    try:
        data = conn.recv(5)
        conn.settimeout(1)
        if data[0] != 0x49 or data[1] != 0x7E:
            print('MagicNo incorrect')
            print('Retrying..')
            print()
            continue
        if data[2] != 0x01:
            print('Type value incorrect')
            print('Retrying..')
            print()
            continue
        filennameLen= data[3]*2**8 + data[4]
        if filennameLen > 1024:
            print('File name too long')
            print('Retrying..')
            print()
            continue
        elif filennameLen< 1:
            print('File name too short')
            print('Retrying..')
            print()
            continue            
    except socket.timeout:
        print('Timed out, took to long to recieve data')
        print('Retrying..')
        print()
        conn.close()
        addr = None 
        continue
    
    try:
        data = conn.recv(filennameLen)
        conn.settimeout(1)
        filename = bytearray()
        for i in range(filennameLen):
            filename.append(data[i])
    except IndexError:
        fileresponse(conn, 0)
        conn.close()
    except socket.timeout:
        fileresponse(conn, 0)
        conn.close()
        
    try:
        data_len = 0
        file = open(filename.decode('ascii'), 'r')
        lines = file.readlines()
        fileData = bytearray()
        for line in lines:
            byte_line = line.encode('utf-8')
            for j in range(len(byte_line)):
                fileData.append(byte_line[j])
                data_len += 1  
                
        fileresponse(conn, 1, data_len, fileData)
        file.close()
        conn.close()
        print('Data from ' + filename.decode('ascii') + ' sent to client in ' + \
              str(data_len) + ' bytes (excluding header).')
        print()
        
    except FileNotFoundError as er:
        fileresponse(conn, 0)
        print('File ' + filename.decode('ascii') + ' not found')
        print('Retrying...')
        print()
        conn.close()
        continue 
        
    
        
        
    
