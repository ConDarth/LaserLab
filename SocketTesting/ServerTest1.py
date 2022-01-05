#
# Server Test 1
#
# Connor Lindsay
#

import socket
import sys

# The default address and port to listen on
DEFAULT_HOST = ''       # All ports
DEFAULT_PORT = 5555     # Arbitrary

host = DEFAULT_HOST
port = DEFAULT_PORT

# Creation and use of the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((host, port))

    connNum = 0
    # Listens for connection, and if disconnected then restarts listening
    while True:
        server.listen()

        print('Listening for Connection %d' % connNum)
        connNum += 1

        # Creates the connection
        serverConn, serverAddr = server.accept()
        with serverConn:
            # Starts the connection
            print('Connected by ', serverAddr)

            while True:
                # Receives the data
                dataIn = serverConn.recv(1024)

                # If data received then return length of string
                if dataIn:
                    txt = dataIn
                    print(txt)
                    serverConn.sendall(txt)
