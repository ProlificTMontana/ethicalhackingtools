import re

import sys

from collections import defaultdict

from datetime import datetime, time


FAILED_LOGIN_PATTERN = re.compile(r"Failed login.*from (\d+\.\d+\.\d+\.\d+)")

LOGIN_TIME_PATTERN = re.compile(r"\[(.*?)\]")


# Define suspicious time window (e.g., midnight to 5am)

SUSPICIOUS_HOURS_START = time(0, 0)

SUSPICIOUS_HOURS_END = time(5, 0)


def is_suspicious_time(log_time_str):

    try:

        dt = datetime.strptime(log_time_str, "%d/%b/%Y:%H:%M:%S %z")

        return SUSPICIOUS_HOURS_START <= dt.time() <= SUSPICIOUS_HOURS_END

    except:

        return False


def analyze_log(file_path):

    failed_login_count = defaultdict(int)

    suspicious_times = []


    with open(file_path, 'r') as f:

        for line in f:

            fail_match = FAILED_LOGIN_PATTERN.search(line)

            if fail_match:

                ip = fail_match.group(1)

                failed_login_count[ip] += 1

            

            time_match = LOGIN_TIME_PATTERN.search(line)

            if time_match:

                log_time_str = time_match.group(1)

                if is_suspicious_time(log_time_str):

                    suspicious_times.append(line.strip())


    print("Summary of suspicious activity found:")

    for ip, count in failed_login_count.items():

        if count > 3:

            print(f"IP {ip} had {count} failed login attempts.")

    if suspicious_times:

        print("\nEntries during suspicious hours (midnight to 5am):")

        for entry in suspicious_times:

            print(f" - {entry}")


def main():

    if len(sys.argv) < 2:

        print("Usage: python log_analysis.py <log_file_path>")

        return

    analyze_log(sys.argv[1])


if __name__ == "__main__":

    main()
