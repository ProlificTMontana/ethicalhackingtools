How it works:

Calculates SHA-256 hashes of specified files and stores them in a JSON file as a baseline. Later, it can check the current hash of these files and compare to the baseline to detect modifications.

How to use:


To initialize hash baseline:

python file_integrity_checker.py init file1 file2

To check for modifications:

python file_integrity_checker.py check

You must run init first before using the check command.
