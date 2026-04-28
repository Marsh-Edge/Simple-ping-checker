# Import functions from ping3 library
from ping3 import verbose_ping, EXCEPTIONS, DEBUG

# Aliases for easier use

v = verbose_ping   # Intermediate verbose ping function
ep = EXCEPTIONS    # Ping function mode with exception handling
dp = DEBUG         # High-detail debug mode for ping

# USER INPUT SECTION
# Source IP (optional – user can press Enter to use default)
ip_source = input("\nEnter your source ip (DEFAULT YOUR IP) : ")

# Destination IP – MUST NOT be empty
while True:
    ip_destination = input("\nEnter your ip (DO NOT ENTER DOMAIN LIKE 'google.com'): ")
    if ip_destination:
        break
    print("Destination IP cannot be empty. Please enter a valid IP.")

# Packet size (default = 54)
ip_size_input = input("\nEnter your size to set (DEFAULT 54) : ")
ip_size = int(ip_size_input) if ip_size_input.strip() != "" else 54

# Packet count (default = 4)
packet_count_input = input("\nEnter your count to set (DEFAULT 4) : ")
packet_count = int(packet_count_input) if packet_count_input.strip() != "" else 4

#   PING FUNCTIONS
def ipPingWithDes(ipdes):
    """Ping only using destination IP."""
    print(f"Your destination ip is {ipdes}\n")
    v(ipdes)


def ipPingWithSrc(ipdes, ipsrc):
    """
    Ping using source IP + destination IP.
    """
    print(f"Your destination ip is {ipdes}\nYour source ip is : {ipsrc}\n")
    ipSource = ipsrc   # local variable (not used later, but kept as requested)
    v(ipdes, src_addr=ipsource)  # WARNING: variable name issue → should be 'ipsrc'


def ipPingWithSize(ipdes, ipsz):
    """
    Ping using destination IP + custom packet size.
    """
    print(f"Your destination ip is : {ipdes}\nYour packet size is : {ipsz}\n")
    ipSize = ipsz  # local variable (not used later)
    v(ipdes, size=ipSize)


def ipPingWithCount(ipdes, pkct):
    """
    Ping using destination IP + custom packet count.
    """
    print(f"Your destination ip is : {ipdes}\nYour packet count is : {pkct}\n")
    packetCount = pkct  # local variable (not used later)
    v(ipdes, count=packetCount)


def ipPing(ipsrc, ipdes, ipsz, pkct):
    """
    Full custom ping: source IP + destination + size + count.
    """
    print(f"""
Your source ip is : {ipsrc}
Your destination ip is : {ipdes}
Your packet size is : {ipsz}
Your packet count is : {pkct}
""")

    # Local variable assignments (not strictly needed, but kept to match original code)
    ipSource = ipsrc
    ipSize = ipsz
    packetCount = pkct

    # Perform ping with all options
    v(ipdes, src_addr=ipSource, size=ipSize, count=packetCount)

#   EXECUTE MAIN PING

ipPing(ip_source, ip_destination, ip_size, packet_count)