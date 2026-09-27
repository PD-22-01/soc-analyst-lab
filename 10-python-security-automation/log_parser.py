"""Simple defensive log parser for SOC training.

This example counts failed authentication events by source IP
from a small text log. Adapt the parser to the actual log format.
"""

from collections import Counter
import re

FAILED_LOGIN = re.compile(
    r"Failed login.*?from\s+(?P<ip>\d{1,3}(?:\.\d{1,3}){3})",
    re.IGNORECASE,
)

def count_failed_logins(lines):
    counts = Counter()

    for line in lines:
        match = FAILED_LOGIN.search(line)
        if match:
            counts[match.group("ip")] += 1

    return counts


if __name__ == "__main__":
    sample_logs = [
        "Failed login for alex from 203.0.113.10",
        "Failed login for alex from 203.0.113.10",
        "Failed login for sam from 198.51.100.20",
    ]

    for ip, count in count_failed_logins(sample_logs).most_common():
        print(f"{ip}: {count} failed login(s)")
