import socket

import sys

from requests.auth import HTTPBasicAuth

import requests


COMMON_PORTS = [80, 8080, 23, 22, 443]  # HTTP, Telnet, SSH, HTTPS, etc.

DEFAULT_CREDS = [

    ("admin", "admin"),

    ("admin", "password"),

    ("root", "root"),

    ("user", "user")

]


def scan_port(ip, port, timeout=1):

    try:

        s = socket.socket()

        s.settimeout(timeout)

        s.connect((ip, port))

        s.close()

        return True

    except:

        return False



def check_default_creds(ip, port):

    url = f"http://{ip}:{port}/"

    for user, pwd in DEFAULT_CREDS:

        try:

            r = requests.get(url, auth=HTTPBasicAuth(user, pwd), timeout=2)

            if r.status_code == 200:

                return user, pwd

        except:

            continue

    return None, None



def main():

    if len(sys.argv) < 2:

        print("Usage: python iot_security_tester.py <IP address>")

        sys.exit(1)


    ip = sys.argv[1]

    print(f"Scanning {ip} for common IoT ports...")


    open_ports = []

    for port in COMMON_PORTS:

        if scan_port(ip, port):

            print(f"Port {port} is open.")

            open_ports.append(port)


    if not open_ports:

        print("No common IoT ports open.")

        return


    print("\nChecking default credentials on HTTP ports found...")

    for port in open_ports:

        if port in (80, 8080):

            user, pwd = check_default_creds(ip, port)

            if user:

                print(f"Default credentials found on {ip}:{port} - Username: {user} Password: {pwd}")

            else:

                print(f"No default credentials found on {ip}:{port}")


if __name__ == "__main__":

    main()
