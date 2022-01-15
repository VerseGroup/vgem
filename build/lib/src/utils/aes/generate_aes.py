# imports
import os

# crypto imports
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def generate_cipher_aes():
    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    return cipher