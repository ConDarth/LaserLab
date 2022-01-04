#
# Client Test 1
#
# Connor Lindsay
#

import socket
import sys

# The default address to connect to
DEFAULT_HOST = '127.0.0.1' # Local Host
DEFAULT_PORT = 5555        # Arbitrary

# Setting the host and port values
# Need to allow for changing this
host = DEFAULT_HOST
port = DEFAULT_PORT

# Creating the socket and then connecting to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((host, port))

    while True:  
        # Getting the data to send out
        dataOut = input().encode('ASCII')
        if dataOut == 'q':
            break
        
        client.sendall(dataOut)

        # Receiving data back from the server
        dataIn = client.recv(1024)
        print(dataIn.decode('ASCII'))
