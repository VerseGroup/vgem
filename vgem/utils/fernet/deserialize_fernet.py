#crypto imports
from cryptography.fernet import Fernet

# python imports
import os
import sys

# adding dir to sys to allow local importing
currentdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(currentdir)
parentdir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentdir)

# local imports
from decrypt import decrypt_private
from base64ec import decode

def deserialize_fernet(key, private_key=None, base64=False):

    if base64:
        key = decode(key)

    if private_key is not None:
        key = decrypt_private(key, private_key)

    return key




    