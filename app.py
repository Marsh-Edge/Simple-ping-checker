from pings.simple_ip_ping import get_source_ip, get_destination_ip, get_packet_size, get_packet_count, ip_ping


def main():
    src = get_source_ip()
    dst = get_destination_ip()
    size = get_packet_size()
    count = get_packet_count()
    ip_ping(src, dst, size, count)


if __name__ == "__main__":
    main()
