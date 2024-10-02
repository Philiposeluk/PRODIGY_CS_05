import socket
import struct
import textwrap
import time

def packet_sniffer(interface):
    # Create a raw socket to capture packets
    try:
        conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))  # For Linux
        # Optionally set the socket to allow for promiscuous mode
        conn.bind((interface, 0))
    except PermissionError:
        print("You need to run this script with administrative privileges.")
        return
    except Exception as e:
        print(f"An error occurred while creating the socket: {e}")
        return

    print("Starting packet sniffer... Press Ctrl+C to stop.")
    
    try:
        while True:
            # Receive packets
            raw_data, addr = conn.recvfrom(65536)
            # Process the packet
            process_packet(raw_data)
    except KeyboardInterrupt:
        print("\nSniffer stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")

def process_packet(raw_data):
    # Unpack the Ethernet header
    eth_length = 14
    eth_header = raw_data[:eth_length]
    eth = struct.unpack('!6s6sH', eth_header)
    
    # Extract protocol
    eth_protocol = socket.ntohs(eth[2])
    
    # Check for IP protocol
    if eth_protocol == 8:
        ip_header = raw_data[eth_length:eth_length + 20]
        ip = struct.unpack('!BBHHHBBH4s4s', ip_header)
       
        # Extract IP addresses
        source_ip = socket.inet_ntoa(ip[8])
        destination_ip = socket.inet_ntoa(ip[9])
        
        # Display packet information
        print(f"\nTime: {time.ctime()}")
        print(f"Source IP: {source_ip}, Destination IP: {destination_ip}, Protocol: {eth_protocol}")
        print(f"Payload Data:\n{format_payload(raw_data[eth_length + 20:])}")

def format_payload(payload):
    # Format the payload for better readability
    return textwrap.indent(repr(payload), '    ')

if __name__ == "__main__":
    interface = "eth0"  # Replace with your actual interface name
    packet_sniffer(interface)
