#!/usr/bin/python3
"""
This module contains a script that reads stdin line by
line and computes metrics.
"""
import sys


file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Prints the file size and the status code counts."""

    print("File size: {}".format(file_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))


try:
    for line in sys.stdin:
        line_count += 1
        tokens = line.split()
        try:
            file_size += int(tokens[-1])
            status_code = int(tokens[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1
        except Exception:
            pass
        if line_count % 10 == 0:
            print_stats()
    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
