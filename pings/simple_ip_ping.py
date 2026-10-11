import re

from pings.utils import run_ping


def validate_ipv4(ip_str):
    pattern = r"^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$"
    return bool(re.match(pattern, ip_str))


def get_source_ip():
    source_ip = input("\nEnter your source IP (DEFAULT YOUR IP) : ").strip()
    return source_ip if source_ip else None


def get_destination_ip():
    while True:
        dest_ip = input("\nEnter your destination IP (DO NOT ENTER DOMAIN LIKE 'google.com'): ").strip()
        if not dest_ip:
            print("Destination IP cannot be empty. Please enter a valid IP.")
            continue
        if not validate_ipv4(dest_ip):
            print("Invalid IPv4 address. Please enter a valid IP (e.g., 8.8.8.8).")
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


def get_interval():
    while True:
        interval_input = input("\nEnter interval between pings in seconds (DEFAULT 1.0) : ").strip()
        if not interval_input:
            return 1.0
        try:
            interval = float(interval_input)
            if interval < 0:
                print("Interval must be non-negative.")
                continue
            return interval
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


def ip_ping(source_ip, dest_ip, packet_size, packet_count, timeout=4, ttl=None, interval=1.0, quiet=False):
    print(f"\nYour source IP is : {source_ip or 'DEFAULT'}")
    print(f"Your destination IP is : {dest_ip}")
    print(f"Your packet size is : {packet_size}")
    print(f"Your packet count is : {packet_count}\n")

    run_ping(
        dst=dest_ip,
        count=packet_count,
        size=packet_size,
        src_addr=source_ip,
        timeout=timeout,
        ttl=ttl,
        interval=interval,
        quiet=quiet,
    )


if __name__ == "__main__":
    src = get_source_ip()
    dst = get_destination_ip()
    size = get_packet_size()
    count = get_packet_count()
    timeout = get_timeout()
    ttl = get_ttl()
    ip_ping(src, dst, size, count, timeout=timeout, ttl=ttl, interval=get_interval())
