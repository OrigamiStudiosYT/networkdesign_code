import socket

# Define server details
SERVER_HOST = "127.0.0.1"  # Localhost
SERVER_PORT = 20825  # Port for server

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

print(f"Server is listening on {SERVER_HOST}:{SERVER_PORT}...")

while True:
    # Receive a message from the client
    MESSAGE, client_address = server_socket.recvfrom(1024)  # Buffer size is 1024 bytes
    print(f"Received message from client {client_address}: {MESSAGE.decode()}")

    # Echo the message back to the client
    server_socket.sendto(MESSAGE, client_address)
    print(f"Echoed message back to client {client_address}")
