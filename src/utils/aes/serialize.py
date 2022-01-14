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
from encrypt import encrypt_private, encrypt_public

def serialize_aes(cipher, public_key=None, private_key=None):
    key = cipher.algorithm.key
    iv = cipher.mode._initialization_vector

    serialized_aes_object = f"START_KEY:{key}END_KEYSTART_IV:{iv}END_IV"

    if public_key is not None:
        serialized_aes_object = encrypt_public(serialized_aes_object, public_key)
    elif private_key is not None:
        serialized_aes_object = encrypt_private(serialized_aes_object, private_key)
    else:
        raise ValueError('NO KEY PASSED')

    return serialized_aes_object
