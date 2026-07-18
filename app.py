from pings.simple_ip_ping import (
    get_source_ip as ip_get_source_ip,
    get_destination_ip,
    get_packet_size as ip_get_packet_size,
    get_packet_count as ip_get_packet_count,
    ip_ping,
)
from pings.simple_domain_ping import (
    get_destination_domain,
    get_packet_size as domain_get_packet_size,
    get_packet_count as domain_get_packet_count,
    domain_ping,
)


def ip_ping_menu():
    src = ip_get_source_ip()
    dst = get_destination_ip()
    size = ip_get_packet_size()
    count = ip_get_packet_count()
    ip_ping(src, dst, size, count)


def domain_ping_menu():
    src = ip_get_source_ip()
    dst = get_destination_domain()
    size = domain_get_packet_size()
    count = domain_get_packet_count()
    domain_ping(src, dst, size, count)


def main():
    print("\n===== Simple Ping Checker =====")
    print("1) IP Ping")
    print("2) Domain Ping")

    while True:
        choice = input("\nChoose an option (1 or 2): ").strip()
        if choice == "1":
            ip_ping_menu()
            break
        elif choice == "2":
            domain_ping_menu()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
