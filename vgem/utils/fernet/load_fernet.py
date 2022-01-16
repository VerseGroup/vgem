#crypto imports
from cryptography.fernet import Fernet

def load_fernet_object(key):
    return Fernet(key)