# python imports
import os
import sys

# adding dir to sys to allow local importing
currentdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(currentdir)
parentdir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentdir)

# crypto imports
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# local imports
from decrypt import decrypt_private
from load_aes import load_cipher

def deserialize_aes(serialized_aes, decrypt, private_key=None):

    if decrypt == True:
        if private_key is not None:
            serialized_aes = decrypt_private(serialized_aes, private_key)
        else: 
            raise ValueError('DECRYPT SET TO TRUE BUT NO KEY PASSED')

    serialized_aes = serialized_aes.split("PARTITION")
    key = serialized_aes[0]
    iv = serialized_aes[1]

    cipher = load_cipher(key, iv)

    return cipher

 