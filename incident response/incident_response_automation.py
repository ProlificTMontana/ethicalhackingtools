import platform

import socket

import subprocess

import os

import datetime


def get_system_info():

    info = {

        "hostname": socket.gethostname(),

        "os": platform.system(),

        "os_version": platform.version(),

        "architecture": platform.machine(),

        "ip_address": socket.gethostbyname(socket.gethostname())

    }

    return info


def get_processes():

    # cross platform approach (Windows / Unix)

    try:

        if os.name == 'nt':

            result = subprocess.check_output(["tasklist"], shell=True, text=True)

        else:

            result = subprocess.check_output(["ps", "aux"], text=True)

    except Exception as e:

        result = f"Failed to get process list: {e}"

    return result


def get_network_connections():

    try:

        if os.name == 'nt':

            result = subprocess.check_output(["netstat", "-an"], shell=True, text=True)

        else:

            result = subprocess.check_output(["netstat", "-tunlp"], text=True)

    except Exception as e:

        result = f"Failed to get netstat info: {e}"

    return result


def get_disk_usage():

    try:

        if os.name == 'nt':

            result = subprocess.check_output(["wmic", "logicaldisk", "get", "size,freespace,caption"], shell=True, text=True)

        else:

            result = subprocess.check_output(["df", "-h"], text=True)

    except Exception as e:

        result = f"Failed to get disk usage: {e}"

    return result


def save_report(report_dir="incident_reports"):

    if not os.path.exists(report_dir):

        os.makedirs(report_dir)


    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = os.path.join(report_dir, f"incident_report_{timestamp}.txt")


    with open(filename, 'w') as f:

        f.write("=== Incident Response Report ===\n\n")


        f.write("== System Information ==\n")

        for k, v in get_system_info().items():

            f.write(f"{k}: {v}\n")


        f.write("\n== Running Processes ==\n")

        f.write(get_processes())


        f.write("\n== Network Connections ==\n")

        f.write(get_network_connections())


        f.write("\n== Disk Usage ==\n")

        f.write(get_disk_usage())


    print(f"Incident report saved to {filename}")


def main():

    print("Starting incident response automation...")

    save_report()


if __name__ == "__main__":

    main()
