"""
Basic Network Sniffer
=====================
A beginner-friendly packet sniffer built with Python and Scapy.
Captures live network traffic and displays key packet information.

CodeAlpha Cyber Security Internship Project
"""

import sys

# Try importing Scapy and handle missing dependency gracefully
try:
    from scapy.all import sniff, IP, TCP, UDP, ICMP
except ImportError:
    print("[ERROR] Scapy is not installed.")
    print("        Run: pip install scapy")
    sys.exit(1)


# Counter to track how many packets have been captured
packet_count = 0


def print_welcome_message():
    """Display a welcome banner when the program starts."""
    print("=" * 60)
    print("       BASIC NETWORK SNIFFER - CodeAlpha Project")
    print("=" * 60)
    print("  Capturing live network packets...")
    print("  Press Ctrl+C to stop the sniffer.")
    print("=" * 60)
    print()


def get_protocol_name(packet):
    """
    Identify the transport-layer protocol of a packet.

    Returns TCP, UDP, ICMP, or Other based on the packet layers.
    """
    if packet.haslayer(TCP):
        return "TCP"
    if packet.haslayer(UDP):
        return "UDP"
    if packet.haslayer(ICMP):
        return "ICMP"
    return "Other"


def process_packet(packet):
    """
    Callback function called for each captured packet.
    Extracts and prints source IP, destination IP, protocol, and summary.
    """
    global packet_count

    # Only process packets that contain an IP layer
    if not packet.haslayer(IP):
        return

    packet_count += 1

    # Extract IP addresses from the IP layer
    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    protocol = get_protocol_name(packet)

    # Build a short summary using Scapy's built-in summary method
    summary = packet.summary()

    # Display packet details in a readable format
    print(f"[Packet #{packet_count}]")
    print(f"  Source IP      : {source_ip}")
    print(f"  Destination IP : {destination_ip}")
    print(f"  Protocol       : {protocol}")
    print(f"  Summary        : {summary}")
    print("-" * 60)


def start_sniffer():
    """
    Start capturing live network packets.
    Uses Scapy's sniff() function with a callback for each packet.
    """
    print_welcome_message()

    try:
        # sniff() captures packets in real time and calls process_packet for each one
        sniff(prn=process_packet, store=False)

    except PermissionError:
        print("\n[ERROR] Permission denied!")
        print("        Run this program as Administrator (Windows)")
        print("        or with sudo (Linux/macOS).")
        sys.exit(1)

    except OSError as error:
        print(f"\n[ERROR] Network interface error: {error}")
        print("        Make sure Npcap (Windows) or libpcap (Linux) is installed.")
        sys.exit(1)

    except KeyboardInterrupt:
        # User pressed Ctrl+C to stop capturing
        print(f"\n[INFO] Sniffer stopped. Total packets captured: {packet_count}")
        print("       Thank you for using Basic Network Sniffer!")

    except Exception as error:
        print(f"\n[ERROR] An unexpected error occurred: {error}")
        sys.exit(1)


if __name__ == "__main__":
    start_sniffer()
