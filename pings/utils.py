import time

from ping3 import ping


def run_ping(dst, count=4, size=56, src_addr=None, timeout=4, quiet=False):
    sent = 0
    received = 0
    latencies = []
    seq = 0

    try:
        while count == 0 or seq < count:
            sent += 1
            kwargs = {"dest_addr": dst, "size": size, "timeout": timeout, "unit": "ms"}
            if src_addr:
                kwargs["src_addr"] = src_addr

            result = ping(**kwargs)

            if result is None:
                if not quiet:
                    print(f"Request timed out. (seq={seq})")
            elif result is False:
                if not quiet:
                    print(f"Destination unreachable. (seq={seq})")
            else:
                received += 1
                latencies.append(result)
                if not quiet:
                    print(f"Reply from {dst}: bytes={size} time={result:.1f}ms")

            seq += 1
            if count == 0 or seq < count:
                time.sleep(0)
    except KeyboardInterrupt:
        if not quiet:
            print("\nStopped by user.")

    loss = sent - received
    loss_pct = (loss / sent) * 100 if sent > 0 else 0

    print("\n--- Ping Statistics ---")
    print(f"{sent} transmitted, {received} received, {loss} lost ({loss_pct:.1f}% loss)")

    if latencies:
        min_lat = min(latencies)
        avg_lat = sum(latencies) / len(latencies)
        max_lat = max(latencies)
        print(f"Min/Avg/Max = {min_lat:.1f} / {avg_lat:.1f} / {max_lat:.1f} ms")
    else:
        print("No successful pings to compute latency.")
