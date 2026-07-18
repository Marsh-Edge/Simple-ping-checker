import re

from pings.utils import resolve_domain, run_ping


def validate_domain(domain):
    if not domain or len(domain) > 253:
        return False
    if domain.startswith(".") or domain.endswith(".") or ".." in domain:
        return False
    ipv4_pattern = r"^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$"
    if re.match(ipv4_pattern, domain):
        return False
    label_pattern = r"^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$"
    labels = domain.split(".")
    return all(re.match(label_pattern, label) and len(label) <= 63 for label in labels)


def get_source_ip():
    source_ip = input("\nEnter your source IP (DEFAULT YOUR IP) : ").strip()
    return source_ip if source_ip else None


def get_destination_domain():
    while True:
        dest_domain = input("\nEnter your domain (DO NOT ENTER IP LIKE '8.8.8.8'): ").strip()
        if not dest_domain:
            print("Destination domain cannot be empty. Please enter a valid domain.")
            continue
        if not validate_domain(dest_domain):
            print("Invalid domain. Please enter a valid domain (e.g., google.com).")
            continue
        return dest_domain


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


def domain_ping(source_ip, dest_domain, packet_size, packet_count, timeout=4, quiet=False):
    print(f"\nYour source IP is : {source_ip or 'DEFAULT'}")
    print(f"Your destination domain is : {dest_domain}")
    print(f"Your packet size is : {packet_size}")
    print(f"Your packet count is : {packet_count}\n")

    resolved_ip = resolve_domain(dest_domain)
    if resolved_ip:
        print(f"Resolved: {dest_domain} -> {resolved_ip}\n")
    else:
        print(f"Failed to resolve: {dest_domain}\n")

    run_ping(
        dst=dest_domain,
        count=packet_count,
        size=packet_size,
        src_addr=source_ip,
        timeout=timeout,
        quiet=quiet,
    )


if __name__ == "__main__":
    src = get_source_ip()
    dst = get_destination_domain()
    size = get_packet_size()
    count = get_packet_count()
    timeout = get_timeout()
    domain_ping(src, dst, size, count, timeout=timeout)
