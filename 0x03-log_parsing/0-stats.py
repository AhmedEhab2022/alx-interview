#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_codes = {str(i): 0 for i in [200, 301, 400, 401, 403, 404, 405, 500]}


def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


# Handle keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

try:
    for i, line in enumerate(sys.stdin, 1):
        try:
            parts = line.split()
            size = int(parts[-1])
            status_code = parts[-2]

            # Update total size and status code count
            total_size += size
            if status_code in status_codes:
                status_codes[status_code] += 1

        except Exception as e:
            pass

        # After every 10 lines, print statistics from the beginning
        if i % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass

finally:
    print_stats()
