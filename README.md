# Packet Sniffer

## Overview

This packet sniffer is a Python tool designed to capture and analyze network packets at the Ethernet level. It displays relevant information such as source and destination IP addresses, protocols, and payload data. The tool is intended for educational purposes and should be used ethically.

## Features

- Captures all network packets on a specified interface.
- Displays source and destination IP addresses.
- Shows the protocol used (e.g., IP).
- Formats payload data for better readability.
- Runs in a continuous loop until interrupted.

## Requirements

- Python 3.x
- Administrative privileges (required for raw socket access)
- Linux operating system

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Philiposeluk/PRODIGY_CS_05
   cd Network_Packet_Analyzer
   
3. **Run the script**: Ensure you have Python installed. You can run the script using:

    ```
    sudo python3 packet_sniffer.py

## Usage 

1. Identify Your Network Interface:Before running the script, identify the correct network interface you want to sniff. You can do this with:

   ```
    ip a
3. Run the Sniffer: Edit the script to set the 'interface' variable to your network interface name (e.g., 'eth0', 'wlan0'):
    ```
    interface = "eth0"  # Replace with your actual interface name
4. Run the script:
   ```
   sudo python3 Network_Packet_Analyzer.py
The sniffer will start capturing packets and display the output in the terminal. Press Ctrl+C to stop the sniffer.

## Example Output 

    ```
    Starting packet sniffer... Press Ctrl+C to stop.

    Time: Mon Oct  3 12:34:56 2023
    Source IP: 192.168.1.10, Destination IP: 192.168.1.5, Protocol: 8
    Payload Data:
      b'\x00\x00\x00\x00\x00\x00...\x00'



