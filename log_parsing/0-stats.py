#!/usr/bin/python3
"""
Module pour analyser les données de logs provenant de stdin.
"""
import sys


def print_stats(total_size, status_codes):
    """
    Print total size
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """
    Lecture stdin + calcul
    """
    total_size = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            tokens = line.split()

            if len(tokens) < 2:
                continue

            file_size = tokens[-1]
            status_code = tokens[-2]

            try:
                total_size += int(file_size)
            except ValueError:
                continue

            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
