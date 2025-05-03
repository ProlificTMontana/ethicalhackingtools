How it works:

Scans a single IP address for common IoT-related open ports (HTTP, Telnet, SSH, etc.). If HTTP ports are found open, it attempts to login with a set of default credentials to identify insecure devices.

How to use:

Run the script with an IP address argument:

python iot_security_tester.py 192.168.1.10

The tool reports open ports and if default credentials are accepted.
