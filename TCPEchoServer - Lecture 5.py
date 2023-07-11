import socket
import sys
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Bind the socket to the port
server_address = ('localhost', 1024)
print('starting up on port ', server_address) 
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept() # Wait for a connection try:
    print('connection from', client_address)
    while True:
    # Receive the data in small chunks and retransmit it
        data = connection.recv(16)
        print('received ', data)
        if data:
            print('sending data back to the client')
            connection.sendall(data)
        else:
            print('no data from', client_address)
            break
    #finally:
    # Clean up the connection
    connection.close()