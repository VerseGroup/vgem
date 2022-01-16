# python imports
from email.mime import base
from json import load
import os
import sys

# adding dir to sys to allow local importing
currentdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(currentdir)

# utils import 
from utils import *

class EM():

    def __init__(self, private_key=None, public_key=None, serialized_private_key=None, serialized_public_key=None, fernet_key=None, encrypted_fernet_key=None):

        # case new keys
        if private_key is None and public_key is None and serialized_private_key is None and serialized_public_key is None:
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

        # loading fernet key if given
        if fernet_key is not None:
            fernets = load_fernet_object(fernet_key)
            self.fernet_key = fernets['key']
            self.fernet = fernets['f']
      
        elif encrypted_fernet_key is not None:
            self.fernet_key = deserialize_fernet(encrypted_fernet_key, self.private_key, True)
            self.fernet = load_fernet_object(self.fernet_key)['f']
        else:
            fernets = generate_fernet_object()
            self.fernet_key = fernets['key']
            self.fernet = fernets['f']

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

    def encrypt_rsa(self, message, base64):

        if self.public_key is not None:
            encrypted_message = encrypt_public(message, self.public_key)

        if base64 == True:
            encrypted_message = encode(encrypted_message)

        return encrypted_message

    def decrypt_rsa(self, message, base64):

        if base64 == True:
            message = decode(message)

        if self.private_key is not None:
            try:
                message = decrypt_private(message, self.private_key)
            except:
                return None

        message = message.decode('utf-8')

        return message

    def encrypt_fernet(self, message, base64):
        
        if self.fernet is not None:
            token = encrypt_fernet(self.fernet, message)
        
        if base64 == True:
            token = encode(token)

        return token

    def decrypt_fernet(self, token, base64):

        if base64 == True:
            token = decode(token)

        if self.fernet is not None:
            try:
                message = decrypt_fernet(self.fernet, token)
            except:
                return None

        return message

    def load_new_fernet(self, key):
        self.fernet = load_fernet_object(key)

    def serialize_fernet(self, encrypt, base64):

        if encrypt==True:
            key = serialize_fernet(self.fernet_key, self.public_key, base64)
        else:
            key = serialize_fernet(key=self.fernet_key, base64=base64)
        
        return key
        
    def deserialize_fernet(self, key, decrypt, base64):

        if decrypt == True:
            key = deserialize_fernet(key, self.private_key, base64)
        else:
            key = deserialize_fernet(key, base64=base64)
        
        fernet = load_fernet_object(key)

        self.fernet = fernet

    