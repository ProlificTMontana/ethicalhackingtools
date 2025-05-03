import hashlib

import os

import json

import sys


HASH_STORE = "file_hashes.json"



def sha256sum(filename):

    h  = hashlib.sha256()

    with open(filename, 'rb') as f:

        for chunk in iter(lambda: f.read(4096), b""):

            h.update(chunk)

    return h.hexdigest()



def init_hashes(file_list):

    hashes = {}

    for file in file_list:

        if os.path.isfile(file):

            hashes[file] = sha256sum(file)

    with open(HASH_STORE, 'w') as f:

        json.dump(hashes, f, indent=2)

    print(f"Initialized hashes and saved to {HASH_STORE}")



def check_hashes():

    if not os.path.exists(HASH_STORE):

        print("Hash store not found. Run init first.")

        return

    with open(HASH_STORE, 'r') as f:

        stored_hashes = json.load(f)


    modified_files = []

    for file, old_hash in stored_hashes.items():

        if not os.path.exists(file):

            print(f"Warning: File missing: {file}")

            modified_files.append(file)

            continue

        current_hash = sha256sum(file)

        if current_hash != old_hash:

            modified_files.append(file)


    if modified_files:

        print("Files with modified contents detected:")

        for file in modified_files:

            print(f" - {file}")

    else:

        print("All files match the stored hashes.")



def main():

    if len(sys.argv) < 2:

        print("Usage: python file_integrity_checker.py init|check file1 [file2 ...]")

        sys.exit(1)


    command = sys.argv[1].lower()

    files = sys.argv[2:]


    if command == 'init':

        if not files:

            print("Provide files to initialize.")

            sys.exit(1)

        init_hashes(files)

    elif command == 'check':

        check_hashes()

    else:

        print("Unknown command. Use 'init' or 'check'.")



if __name__ == "__main__":

    main()
