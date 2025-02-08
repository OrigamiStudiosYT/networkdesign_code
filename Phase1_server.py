import socket

# Define server details
SERVER_HOST = "127.0.0.1"  # Localhost
SERVER_PORT = 20825  # Port number for the server

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

print(f"Server is listening on {SERVER_HOST}:{SERVER_PORT}...")

while True:
    # Receive a message from the client
    message, client_address = server_socket.recvfrom(1024)  # Buffer size is 1024 bytes
    print(f"Received message from client {client_address}: {message.decode()}")

    # Echo the message back to the client
    server_socket.sendto(message, client_address)
    print(f"Echoed message back to client {client_address}")
