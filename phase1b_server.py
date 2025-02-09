import socket

def udp_server(output_file, server_port=20825):
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("127.0.0.1", server_port))
    
    print(f"Server is listening on port {server_port}...")
    
    received_packets = {}
    while True:
        # Receive a packet
        packet, client_address = server_socket.recvfrom(2048)
        
        # Extract sequence number and data
        seq_no = int.from_bytes(packet[:4], "big")
        data = packet[4:]
        
        # Store the packet data
        received_packets[seq_no] = data
        print(f"Received packet #{seq_no} from {client_address}")
        
        # Send acknowledgment
        server_socket.sendto(seq_no.to_bytes(4, "big"), client_address)
        
        # Check if it's the last packet (data < 1024 bytes indicates the end)
        if len(data) < 1024:
            break
    
    # Reassemble the file
    with open(output_file, "wb") as f:
        for seq_no in sorted(received_packets.keys()):
            f.write(received_packets[seq_no])
    print(f"File transfer complete. File saved as {output_file}")

# Run the server
udp_server("output.bmp")
