# Import functions from ping3 library
from ping3 import verbose_ping, EXCEPTIONS, DEBUG

# Aliases for easier use
v = verbose_ping   # Intermediate verbose ping function
ep = EXCEPTIONS    # Ping function mode with exception handling
dp = DEBUG         # High-detail debug mode for ping

# USER INPUT SECTION
# Source IP (optional - user can leave empty)
ip_source = input("\nEnter your source IP (DEFAULT YOUR IP) : ")

# Destination Domain validation loop
while True:
    domain_destination = input(
        "\nEnter your domain (DO NOT ENTER IP LIKE '8.8.8.8'): "
    ).strip()

    # Prevent empty input
    if not domain_destination:
        print("Destination domain cannot be empty. Please enter a valid domain.")
        continue

    # Prevent numbers only
    if domain_destination.isdigit():
        print("Do not enter numbers only. Please enter a valid domain name.")
        continue

    # Detect if user entered an IPv4 address instead of a domain
    parts = domain_destination.split(".")
    if len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts):
        print("Do not enter an IP address. Please enter a domain name (e.g., google.com).")
        continue

    # Basic domain format validation
    if "." not in domain_destination or domain_destination.startswith(".") or domain_destination.endswith("."):
        print("Invalid domain format. Example: example.com")
        continue

    break


# Packet size input (default = 54 bytes)
domain_size_input = input("\nEnter your size to set (DEFAULT 54) : ")
domain_size = int(domain_size_input) if domain_size_input.strip() != "" else 54


# Packet count input (default = 4 packets)
domain_count_input = input("\nEnter your count to set (DEFAULT 4) : ")
packet_count = int(domain_count_input) if domain_count_input.strip() != "" else 4

#   PING FUNCTIONS
def ipPingWithDes(ddes):
    """
    Ping only with destination domain
    """
    print(f"Your destination domain is {ddes}\n")
    v(ddes)


def ipPingWithSrc(ddes, ipsrc):
    """
    Ping with custom source IP and destination domain
    """
    print(f"Your destination domain is {ddes}\nYour source domain is : {ipsrc}\n")

    # Local variable assignment
    ipSource = ipsrc

    # Perform ping
    v(ddes, src_addr=ipSource)


def ipPingWithSize(ddes, dsz):
    """
    Ping with custom packet size
    """
    print(f"Your destination domain is : {ddes}\nYour packet size is : {dsz}\n")

    dSize = dsz
    v(ddes, size=dSize)


def ipPingWithCount(ddes, pkct):
    """
    Ping with custom packet count
    """
    print(f"Your destination domain is : {ddes}\nYour packet count is : {pkct}\n")

    packetCount = pkct
    v(ddes, count=packetCount)


def ipPing(ipsrc, ddes, dsz, pkct):
    """
    Full ping configuration:
    source IP + destination domain + size + packet count
    """

    print(
        f"\nYour source IP is : {ipsrc}"
        f"\nYour destination domain is : {ddes}"
        f"\nYour packet size is : {dsz}"
        f"\nYour packet count is : {pkct}\n"
    )

    # Assign parameters to local variables
    ipSource = ipsrc
    dSize = dsz
    packetCount = pkct

    # Execute verbose ping
    v(ddes, src_addr=ipSource, size=dSize, count=packetCount)

#   EXECUTE MAIN PING

ipPing(ip_source, domain_destination, domain_size, packet_count)