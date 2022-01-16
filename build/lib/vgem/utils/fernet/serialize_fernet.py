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
from encrypt import encrypt_public
from base64ec import encode

def serialize_fernet(key, public_key=None, base64=False):

    if public_key is not None:
        key = encrypt_public(key, public_key, False)

    if base64:
        key = encode(key)

    return key
