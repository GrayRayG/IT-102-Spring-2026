#!/usr/bin/env python3
# Script that scans web server logs for status codes
# Use RegEx to find and report on most frequent status messages
# By Ray G Peckham

"""
This is for counting status codes
"""

#Libraries
import re
from collections import defaultdict

def main():
    LOG_FILE = r"/Users/raygpeckham/IT-102-Spring-2026/start/CH07/access.log"
    counts = defaultdict(int)

    with open (LOG_FILE, "r") as f:
        for line in f:
            match = re.search(r'" (\d{3}) ', line)
            if match:
                counts[match.group(1)] += 1

    for code, count in sorted(counts.items()):
        print(f"{code}: {count}")

if __name__ == "__main__":
    main()