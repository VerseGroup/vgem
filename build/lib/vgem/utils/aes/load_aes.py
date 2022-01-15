# crypto imports
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def load_cipher(key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    return cipher
