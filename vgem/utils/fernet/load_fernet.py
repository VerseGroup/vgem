#crypto imports
from cryptography.fernet import Fernet

def load_fernet_object(key):
    f = Fernet(key)
    return {"f" : f, "key" : key}
    