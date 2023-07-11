import socket
import sys
# Create a TCP/IP socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Connect the socket to the server rlistening port
server_address = ('localhost', 1024)
sock.connect(server_address)
try:
    # Send data
    message = 'This is the message.'
    print('sending ', message) 
    sock.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    msg = []
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data) 
        msg.append(data) 
        print('received ', b''.join(msg).decode())
finally: 
    print('closing socket')
    sock.close()