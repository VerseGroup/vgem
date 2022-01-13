# python imports
import os
import sys

# adding dir to sys to allow local importing
currentdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(currentdir)

# utils import 
# adding local imports to allow shorter imports
from utils import (encode, decode, decrypt_private, encrypt_private, 
                    encrypt_public, serialize_private_key, 
                    serialize_public_key, deserialize_private_key, 
                    deserialize_public_key, generate_private, generate_public)

class EM():

    def __init__(self, private_key=None, public_key=None, serialized_private_key=None, serialized_public_key=None):

        # case new keys
        if private_key is None and public_key is None and serialized_private_key is None and serialize_public_key is None:
            self.private_key = generate_private() 
            self.public_key = generate_public(self.private_key)

        # case private key
        elif private_key is not None:
            self.private_key = private_key
            self.public_key = generate_public(private_key)

        # case serialized private
        elif serialized_private_key is not None:
            self.private_key = deserialize_private_key(serialized_private_key)
            self.public_key = generate_public(self.private_key)

        # case public key
        elif public_key is not None:
            self.public_key = public_key
            self.private_key = None

        # case serialized public
        elif serialized_public_key is not None:
            self.public_key = deserialize_public_key(serialized_public_key)
            self.private_key = None

    def serialize_private_key(self):
        if self.private_key is not None:
            return serialize_private_key(self.private_key)
        else:
            return None

    def serialize_public_key(self):
        if self.public_key is not None:
            return serialize_public_key(self.public_key)
        else:
            return None

    def encrypt_rsa(self, message):
        if self.private_key is not None:
            return encrypt_private(message, self.private_key)
        elif self.public_key is not None:
            return encrypt_public(message, self.public_key)

    def decrypt_rsa(self, message):
        if self.private_key is not None:
            return decrypt_private(message, self.private_key)