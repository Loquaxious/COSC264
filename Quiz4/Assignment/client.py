import socket

port = None

def addr_check(addr):
    try:
        addrinfo = socket.getaddrinfo(addr, port)
        return addrinfo[0][4][0]
    except socket.error:
        print('Address wrong or not correctly formatted')
        print('Quitting...')
        quit()
        
def port_check(port):
    try:
        port = int(port)
        if port < 1024 or port > 64000:
            print('Integer should be between 1024 and 64000')
            print('Quitting...')
            quit()
        else:
            return port
    except ValueError as er:
        print('Value entered should be an integer')
        print('Quitting...')
        quit()
        
def file_check(file):
    try:
        o_file = open(file)
        print('File with this name already found in directory')
        print('Quitting...')
        o_file.close()
        quit()        
    except FileNotFoundError:
        return file

addr = None
port = None
file = None

try:
    addr, port, file = map(str,input('Enter address, port and file seperated by spaces:\n').split())
except ValueError as er:
    print(er)
    print('Quitting...')
    quit()

addr = addr_check(addr)
port = port_check(port)
file = file_check(file)    

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
except socket.error:
    print('Failed to create socket')
    print('Quitting...')
    s.close()
    quit()
try:
    s.connect((addr, port))
except socket.error:
    print('Connection to server timed out')
    print('Quitting...')
    s.close()
    quit()
    
file_request = bytearray(5)
file_request[0] = 0x49
file_request[1] = 0x7E
file_request[2] = 0x01
filenameLen = len(file)
if filenameLen < 1 and filenameLen > 1024:
    print('Filename Length is invlaid')
    print('Quitting...')
    s.close()
    quit()
else:
    file_request[3] = filenameLen >> 8
    file_request[4] = filenameLen & 0x00FF
    filename_bytes = bytes(file, 'utf-8')
    for i in range(filenameLen):
        file_request.append(filename_bytes[i])
    s.sendall(file_request)

try:
    data = s.recv(8)
    s.settimeout(1)
    if data[0] != 0x49 or data[1] != 0x7E:
        print('Incorrect MagicNo')
        print('Quitting...')
        s.close()
        quit()
    if data[2] != 0x02:
        print('Incorrect Type')
        print('Quitting...')
        s.close()
        quit()
    filennameLen= data[3]*2**8 + data[4]
    if data[3] == 0:
        print('File unable to be opened on server side')
        print('Quitting...')
        s.close()
        quit()
    file_data_len = data[4]*2**(24) + data[5]*2**16 + data[6]*2**8 + data[7]
    if file_data_len < 1:
        print('File has no data')
        print('Quitting...')
        s.close()
        quit()
        
except socket.timeout:
    print('Took to long to gather response file header')
    print('Quitting...')
    s.close()
    quit()
    
try:
    w_file = open(file, 'w')
    byte_count = 0

    
    data = s.recv(4096)
    s.settimeout(1)
    while data:
        file_data = bytearray()
        for i in range(len(data)):
            file_data.append(data[i])
            byte_count += 1
        w_file.write(file_data.decode('ascii'))
        data = s.recv(4096)
        s.settimeout(1)
        
    if byte_count < file_data_len:
        print('Error:')
        print('Bytes written to local file is less than file length')
        print('Quitting...')
        s.close()
        w_file.close()
        quit()
    elif byte_count > file_data_len:
        print('Error:')
        print('Bytes written to local file is more than file length')
        print('Quitting...')
        s.close()
        w_file.close()
        quit()
    
    print()
    print('Received data written to local file sucessfully')
    print('Total bytes written: ' + str(byte_count))
    print('Completed and exitting...')
    w_file.close()
    s.close()
    quit()
        
except socket.timeout:
    print('Took to long to gather response file data')
    print('Quitting...')
    s.close()
    w_file.close()
    quit()   
except FileExistsError:
    print('The given file already exists')
    print('Quitting...')
    s.close()
    quit()

        




    
    

    
    
    
