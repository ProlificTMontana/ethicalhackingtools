import os

import json

from cryptography.fernet import Fernet

import base64

import secrets

import string


KEY_FILE = "password_manager.key"

DATA_FILE = "passwords.json"



def generate_key():

    key = Fernet.generate_key()

    with open(KEY_FILE, 'wb') as f:

        f.write(key)

    return key



def load_key():

    if not os.path.exists(KEY_FILE):

        return generate_key()

    with open(KEY_FILE, 'rb') as f:

        return f.read()



def encrypt_password(fernet, password):

    return fernet.encrypt(password.encode()).decode()



def decrypt_password(fernet, token):

    return fernet.decrypt(token.encode()).decode()



def load_passwords():

    if not os.path.exists(DATA_FILE):

        return {}

    with open(DATA_FILE, 'r') as f:

        return json.load(f)



def save_passwords(passwords):

    with open(DATA_FILE, 'w') as f:

        json.dump(passwords, f)



def generate_password(length=16):

    alphabet = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(alphabet) for _ in range(length))

    return password



def main():

    key = load_key()

    fernet = Fernet(key)

    passwords = load_passwords()


    while True:

        print("\nPassword Manager")

        print("1. Generate and save password")

        print("2. Retrieve password")

        print("3. Exit")

        choice = input("Choose an option: ").strip()


        if choice == '1':

            label = input("Enter label for password (e.g. Gmail): ").strip()

            length = input("Enter password length (default 16): ").strip()

            length = int(length) if length.isdigit() and int(length) > 0 else 16

            pwd = generate_password(length)

            enc_pwd = encrypt_password(fernet, pwd)

            passwords[label] = enc_pwd

            save_passwords(passwords)

            print(f"Password for '{label}' saved: {pwd} (keep it safe!)")


        elif choice == '2':

            label = input("Enter label to retrieve password: ").strip()

            if label in passwords:

                try:

                    dec_pwd = decrypt_password(fernet, passwords[label])

                    print(f"Password for '{label}': {dec_pwd}")

                except Exception as e:

                    print("Failed to decrypt password:", e)

            else:

                print("No password found for that label.")


        elif choice == '3':

            print("Exiting.")

            break


        else:

            print("Invalid option. Try again.")



if __name__ == "__main__":

    main()
