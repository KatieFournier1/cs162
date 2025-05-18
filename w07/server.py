# Katie Fournier
# CS 162 Server Assignment
# server.py


import socket


HOST = "127.0.0.1"
PORT = 55555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    # Wait for a client to connect
    print(f'Listening on {HOST}:{PORT}')
    sock.listen()
    connection, _ = sock.accept()
    with connection:
        print(f"Client connected on {HOST}:{PORT}")
        while True:
            # Wait until we receive data
            data = connection.recv(1024)
            print(f"Received {data!r}")
            # Stop the server if the client sends an empty byte (closes the connection)
            if not data:
                break
            # Echoes the data from the client back to the client
            connection.sendall(data)
