# python imports
import os
import sys

from src.utils.aes.serialize_aes import serialize_aes

# adding dir to sys to allow local importing
currentdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(currentdir)
parentdir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentdir)

# crypto imports
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# local imports
from decrypt import decrypt_private

def deserialize_aes(serialized_aes, decrypt, private_key=None):

    if decrypt == True:
        if private_key is not None:
            serialized_aes = decrypt_private(serialized_aes, private_key)
        else: 
            raise ValueError('DECRYPT SET TO TRUE BUT NO KEY PASSED')

    '''

    key = cipher.algorithm.key
    iv = cipher.mode._initialization_vector

    serialized_aes_object = f"START_KEY:{key}END_KEYSTART_IV:{iv}END_IV"
            

    return serialized_aes_object

    '''

 