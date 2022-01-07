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

# Checking For any command aruments
# [options] [IPv4 address] [Port] 
#
# Options:
# -d [IP address] [Port]
#   Sets a default address and port to connect to
#
# -r
#   Resets the default address to the predefined defaults

if len(sys.argv) == 1:
    # If no arguments just use the defaults
    # If no defaults found use system default and set the defaults
    try:
        with open('clientDefault.txt', 'r') as f:
            host = f.readline().strip()
            port = int(f.readline().strip())
    except FileNotFoundError or ValueError:
        host = DEFAULT_HOST 
        port = DEFAULT_PORT

        with open('clientDefault.txt', 'w') as f:
            f.write(host + '\n' + str(port))
else:
    if sys.argv[1] == '-r':
        # Resets to the system default address and port
        host = DEFAULT_HOST 
        port = DEFAULT_PORT

        with open('clientDefault.txt', 'w') as f:
            f.write(host + '\n' + str(port))
            
    elif sys.argv[1] == '-d':
        # Sets new default to use
        try:
            # Needs to make sure there are enough arguments for this
            host = sys.argv[2]
            port = int(sys.argv[3])
            with open('clientDefault.txt', 'w') as f:
                f.write(host + '\n' + str(port))

        except ValueError:
            print('\nValue Error: Invalid value for port')
            print('Port number must be an integer\n')
            exit(1)
        except IndexError:
            print('\nIndex Error: Invalid number of arguments')
            print('Must give an IPv4 address and port number for default\n')
            exit(1)
    else:
        # If no options given use the first two inputs as IPv4 address and port
        host = sys.argv[1]
        
        try:
            # Attempts tp get port number as well
            port = int(sys.argv[2])
            
        except IndexError:
            port = DEFAULT_PORT
        except ValueError:
            print('\nValue Error: Invalid value for port')
            print('Port number must be an integer\n')
            exit(1)
            

# Creating the socket and then connecting to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    try:
        client.connect((host, port))
    except TimeoutError:
        print('\nTimeout Error: Party did not respond in time', file=sys.stderr)
        print('Please check IP address/port and make sure connection not blocked\n', file=sys.stderr)
        exit(1)
    except ConnectionRefusedError:
        print('\nConnection Refused Error: The connection was forcibly blocked', file=sys.stderr)
        print('Make sure the server is active, and accessible\n', file=sys.stderr)
        exit(1)

    while True:
        # Getting the data to send out
        dataOut = input().encode('ASCII')
        client.sendall(dataOut)
        if dataOut == b'q':
            break

        # Receiving data back from the server
        dataIn = client.recv(1024)
        print(dataIn.decode('ASCII'))
