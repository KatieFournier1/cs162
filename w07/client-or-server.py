# Katie Fournier
# CS 162 Server Assignment


import sys
import socket


this_script = sys.argv[0] if sys.argv[0] != '' else 'client-or-server.py'
usage_message = ((
    'A tiny demo of a web server in Python. This script can act as the client or the server.\n\n'
    'Usage:\n'
    f'  python {this_script} (-s | --server)\n'
    f'  python {this_script} (-c | --client)\n'
    f'  python {this_script} [-h | --help]\n\n'
    'Example:\n'
    f'  python {this_script} -s'
))

# Command line argument -s or -c is required.
if (sys.argv[0] == '') or (len(sys.argv) < 2) or (sys.argv[1] in ['-h', '--help']):
    print(usage_message)
    sys.exit(1)


# -- Server --------------------------------------------------------------------

def run_server():
    """Run as a server. Echoes all data received."""

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


# -- Client --------------------------------------------------------------------

def run_client():
    """Run as a client. Connect to the server, send a message, print the reply, then close."""

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


# -- __main__ ------------------------------------------------------------------

def quit_with_usage_message():
        print(usage_message)
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        quit_with_usage_message()
    mode = sys.argv[1]
    if mode in ['-s', '--server']:
        run_server()
    elif mode in ['-c', '--client']:
        run_client()
    else:
        quit_with_usage_message()


