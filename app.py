from pings.simple_ip_ping import (
    get_source_ip,
    get_destination_ip,
    get_packet_size,
    get_packet_count,
    get_timeout,
    get_ttl,
    ip_ping,
)
from pings.simple_ipv6_ping import (
    get_destination_ipv6,
    ipv6_ping,
)
from pings.simple_domain_ping import (
    get_destination_domain,
    domain_ping,
)


def ip_ping_menu(quiet=False):
    src = get_source_ip()
    dst = get_destination_ip()
    size = get_packet_size()
    count = get_packet_count()
    timeout = get_timeout()
    ttl = get_ttl()
    ip_ping(src, dst, size, count, timeout=timeout, ttl=ttl, quiet=quiet)


def ipv6_ping_menu(quiet=False):
    src = get_source_ip()
    dst = get_destination_ipv6()
    size = get_packet_size()
    count = get_packet_count()
    timeout = get_timeout()
    ttl = get_ttl()
    ipv6_ping(src, dst, size, count, timeout=timeout, ttl=ttl, quiet=quiet)


def domain_ping_menu(quiet=False):
    src = get_source_ip()
    dst = get_destination_domain()
    size = get_packet_size()
    count = get_packet_count()
    timeout = get_timeout()
    ttl = get_ttl()
    domain_ping(src, dst, size, count, timeout=timeout, ttl=ttl, quiet=quiet)


def main():
    print("\n===== Simple Ping Checker =====")
    print("1) IPv4 Ping")
    print("2) Domain Ping")
    print("3) IPv4 Ping (Quiet Mode)")
    print("4) Domain Ping (Quiet Mode)")
    print("5) IPv6 Ping")
    print("6) IPv6 Ping (Quiet Mode)")

    while True:
        choice = input("\nChoose an option (1-6): ").strip()
        if choice == "1":
            ip_ping_menu()
            break
        elif choice == "2":
            domain_ping_menu()
            break
        elif choice == "3":
            ip_ping_menu(quiet=True)
            break
        elif choice == "4":
            domain_ping_menu(quiet=True)
            break
        elif choice == "5":
            ipv6_ping_menu()
            break
        elif choice == "6":
            ipv6_ping_menu(quiet=True)
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")


if __name__ == "__main__":
    main()
