Ethical Hacking Tools:

This project contains a collection of standalone Python scripts implementing various ethical hacking and security testing tools. Each tool helps in understanding and practicing cybersecurity concepts in an ethical and legal manner. Make sure to use these tools only on systems and data you have permission to test.

Tools Overview:

Password Manager (`password_manager.py`)

A simple secure password manager that encrypts and stores passwords locally using the `cryptography` library. It can generate strong passwords, save them with labels, and retrieve decrypted passwords for use.

Phishing Detection Tool (`phishing_detection.py`)

Analyzes URLs or email texts to detect potential phishing attempts using simple heuristic checks including suspicious domain names and keyword spotting. (Note: A simple heuristic approach for demonstration).

File Integrity Checker (`file_integrity_checker.py`)

Monitors files for unauthorized changes by calculating and storing SHA-256 hashes. Can verify file integrity later to detect modifications or tampering.

IoT Device Security Tester (`iot_security_tester.py`)

Scans an IP range or specific IP to identify open ports and common default credentials on IoT devices. Helps assess basic IoT device security posture.

Log Analysis Tool (`log_analysis.py`)

Analyzes system or application logs for suspicious patterns such as repeated failed logins or unusual access times, reporting potential security events.

API Security Tester (`api_security_tester.py`)

Tests a RESTful API endpoint for common security issues such as missing authentication, data leakage, improper methods, and basic rate limiting checks.

Steganography Tool (`steganography_tool.py`)

Hides text messages inside an image file and can also extract hidden messages. Demonstrates basic image-based steganography using least significant bit (LSB) manipulation.

Incident Response Automation (`incident_response_automation.py`)

Automates collection of useful forensic data during a security incident such as system info, running processes, network connections, and saves this data to reports for analysis.

---

 Usage

Each tool script is standalone. You can run them from the command line and follow prompts or modify the code for your specific testing needs.

Requirements

Some tools require external Python packages. You can install them via:

```bash

pip install cryptography requests Pillow

```


#Ethical Use Notice

Always ensure you have explicit permission to test targets before running these tools. Unauthorized use can be illegal and unethical.

Contributions to improve these tools or add new ones are welcome!
