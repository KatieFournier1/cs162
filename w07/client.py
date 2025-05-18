# Katie Fournier
# CS 162 Server Assignment
# client.py


import sys
import socket


HOST = "127.0.0.1"
PORT = 55555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to a local server
    try:
        sock.connect((HOST, PORT))
    except ConnectionRefusedError:
        print('Client requires server to be started first.')
        sys.exit()

    print(f"Connected to server at {HOST}:{PORT}")
    # Send a message
    sock.sendall(b"Echo-o-o-o!")
    # Wait for a reply
    data = sock.recv(1024)

print(f"Received {data!r}")
