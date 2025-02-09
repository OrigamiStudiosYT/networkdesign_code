import socket

def make_packet(file_path, packet_size=1024):
    packets = []
    with open(file_path, "rb") as f:
        data = f.read()
        total_packets = len(data) // packet_size + (1 if len(data) % packet_size else 0)
        for i in range(total_packets):
            start = i * packet_size
            end = start + packet_size
            payload = data[start:end]
            packet = {
                "seq_no": i,  # Sequence number
                "data": payload  # Binary data
            }
            packets.append(packet)
    return packets

def udp_client(file_path, server_address=("127.0.0.1", 20825)):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Create packets
    packets = make_packet(file_path)
    
    for packet in packets:
        seq_no = packet["seq_no"]
        data = packet["data"]
        message = seq_no.to_bytes(4, "big") + data  # Add sequence number
        client_socket.sendto(message, server_address)
        print(f"Sent packet #{seq_no}")
        
        # Wait for acknowledgment
        ack, _ = client_socket.recvfrom(4)
        ack_seq_no = int.from_bytes(ack, "big")
        if ack_seq_no != seq_no:
            print(f"Packet #{seq_no} lost. Retrying...")
            client_socket.sendto(message, server_address)
    
    print("File transfer completed.")
    client_socket.close()

# Run the client
udp_client("input.bmp")
