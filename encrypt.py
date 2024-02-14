import os
from cryptography.fernet import Fernet
from pyminizip import compress

def protect_key(key_name):
    pw = input("Enter password for key.key: ")
    name = key_name.replace(".key", "")
    zip_file = f"{name}.zip"

    # Compress the file with password protection
    compress(key_name, None, zip_file, pw, 1)

    print(f"File compressed and password protected as {zip_file}")


def save_key(filename):
    """
    Saves key to a file, but does nothing if the key already exists.
    """
    key = Fernet.generate_key()
    if not os.path.exists(filename):
        with open(filename, "wb") as f:
            f.write(key)
            print(f"Saved content to {filename}")
            print(f"KEY: {key}")
            print("------------------------------ Now set a password for the key --------------------------")
            protect_key(filename)
    else:
        print(f"File -> {filename} <- already exists, skipping save.")

def crypt(bitwarden_csv, key_name):
    # opening the key
    with open(key_name, 'rb') as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)

    # opening the original file to encrypt
    with open(bitwarden_csv, 'rb') as file:
        original = file.read()

    # encrypting the file
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and 
    # writing the encrypted data
    with open(bitwarden_csv, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print(f"File -> {bitwarden_csv} <- encrypted.")

def delete_key(key_name):
    os.remove(key_name)

if __name__ == "__main__":
    bitwarden_csv = "bitwarden.csv"
    key_name = "bitwarden.key"
    save_key(key_name)
    crypt(bitwarden_csv, key_name)
    delete_key(key_name)
