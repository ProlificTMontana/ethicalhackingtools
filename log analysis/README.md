How it works:

Parses a provided log file looking for suspicious patterns such as multiple failed login attempts from the same IP address or accesses during unusual hours (midnight to 5 AM). Reports IPs with excessive failures and entries during suspicious times.

How to use:

Run with a log file path argument:

python log_analysis.py /path/to/logfile.log

It outputs summaries about suspicious activities found.
