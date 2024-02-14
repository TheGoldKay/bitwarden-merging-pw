import os
from cryptography.fernet import Fernet

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
    else:
        print(f"File -> {filename} <- already exists, skipping save.")



if __name__ == "__main__":
    save_key("fileKey.key")
