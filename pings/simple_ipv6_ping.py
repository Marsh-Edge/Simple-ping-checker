import ipaddress

from pings.utils import run_ping


def validate_ipv6(ip_str):
    try:
        addr = ipaddress.ip_address(ip_str)
        return addr.version == 6
    except ValueError:
        return False


def get_source_ip():
    source_ip = input("\nEnter your source IP (DEFAULT YOUR IP) : ").strip()
    return source_ip if source_ip else None


def get_destination_ipv6():
    while True:
        dest_ip = input("\nEnter your destination IPv6 (e.g., fd00::1 or 2001:db8::1): ").strip()
        if not dest_ip:
            print("Destination IPv6 cannot be empty. Please enter a valid IPv6 address.")
            continue
        if not validate_ipv6(dest_ip):
            print("Invalid IPv6 address. Please enter a valid IPv6 (e.g., fd00::1).")
            continue
        return dest_ip


def get_packet_size():
    while True:
        size_input = input("\nEnter packet size in bytes (DEFAULT 54) : ").strip()
        if not size_input:
            return 54
        try:
            size = int(size_input)
            if size <= 0:
                print("Size must be a positive integer.")
                continue
            return size
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_packet_count():
    while True:
        count_input = input("\nEnter packet count (0 for continuous, DEFAULT 4) : ").strip()
        if not count_input:
            return 4
        try:
            count = int(count_input)
            if count < 0:
                print("Count must be 0 or a positive integer.")
                continue
            return count
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_timeout():
    while True:
        timeout_input = input("\nEnter timeout in seconds (DEFAULT 4) : ").strip()
        if not timeout_input:
            return 4
        try:
            timeout = int(timeout_input)
            if timeout <= 0:
                print("Timeout must be a positive integer.")
                continue
            return timeout
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_ttl():
    while True:
        ttl_input = input("\nEnter TTL (DEFAULT OS: 64 on Linux/macOS, 128 on Windows) : ").strip()
        if not ttl_input:
            return None
        try:
            ttl = int(ttl_input)
            if ttl <= 0:
                print("TTL must be a positive integer.")
                continue
            return ttl
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def ipv6_ping(source_ip, dest_ip, packet_size, packet_count, timeout=4, ttl=None, quiet=False):
    print(f"\nYour source IP is : {source_ip or 'DEFAULT'}")
    print(f"Your destination IPv6 is : {dest_ip}")
    print(f"Your packet size is : {packet_size}")
    print(f"Your packet count is : {packet_count}\n")

    run_ping(
        dst=dest_ip,
        count=packet_count,
        size=packet_size,
        src_addr=source_ip,
        timeout=timeout,
        ttl=ttl,
        quiet=quiet,
    )


if __name__ == "__main__":
    src = get_source_ip()
    dst = get_destination_ipv6()
    size = get_packet_size()
    count = get_packet_count()
    timeout = get_timeout()
    ttl = get_ttl()
    ipv6_ping(src, dst, size, count, timeout=timeout, ttl=ttl)
