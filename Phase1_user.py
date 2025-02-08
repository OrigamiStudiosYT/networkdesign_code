import socket

# Define client details
SERVER_HOST = "127.0.0.1"  # Address server
SERVER_PORT = 20825  # Port for server
CLIENT_PORT = 54321  # Port for client

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the client socket to its address and port
client_socket.bind(("127.0.0.1", CLIENT_PORT))

# Message to send
message = "HELLO"

# Send the message to the server
client_socket.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))
print(f"Sent message to server: {message}")

# Receive the echoed message from the server
response, server_address = client_socket.recvfrom(1024)  # Buffer size is 1024 bytes
print(f"Received echoed message from server {server_address}: {response.decode()}")

# Close the socket
client_socket.close()
