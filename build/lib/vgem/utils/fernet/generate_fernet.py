#crypto imports
from cryptography.fernet import Fernet

def generate_fernet_key():
    return Fernet.generate_key()

def generate_fernet_object():
    key = generate_fernet_key()
    f = Fernet(key)
    return {"f" : f, "key" : key}
