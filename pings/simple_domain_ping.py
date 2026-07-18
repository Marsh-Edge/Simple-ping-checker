import re

from ping3 import verbose_ping


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
        count_input = input("\nEnter packet count (DEFAULT 4) : ").strip()
        if not count_input:
            return 4
        try:
            count = int(count_input)
            if count <= 0:
                print("Count must be a positive integer.")
                continue
            return count
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def domain_ping(source_ip, dest_domain, packet_size, packet_count):
    ping_kwargs = {"dst": dest_domain, "size": packet_size, "count": packet_count}

    print(f"\nYour source IP is : {source_ip or 'DEFAULT'}")
    print(f"Your destination domain is : {dest_domain}")
    print(f"Your packet size is : {packet_size}")
    print(f"Your packet count is : {packet_count}\n")

    if source_ip:
        ping_kwargs["src_addr"] = source_ip

    verbose_ping(**ping_kwargs)


if __name__ == "__main__":
    src = get_source_ip()
    dst = get_destination_domain()
    size = get_packet_size()
    count = get_packet_count()
    domain_ping(src, dst, size, count)
