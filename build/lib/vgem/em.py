# python imports
import os
import sys

# adding dir to sys to allow local importing
currentdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(currentdir)

# utils import 
# adding local imports to allow shorter imports
from utils import (encode, decode, decrypt_private, 
                    encrypt_public, serialize_private_key, 
                    serialize_public_key, deserialize_private_key, 
                    deserialize_public_key, generate_private, generate_public,
                    encrypt_aes, decrypt_aes, generate_cipher_aes, load_cipher, 
                    serialize_aes, deserialize_aes)

class EM():

    def __init__(self, private_key=None, public_key=None, serialized_private_key=None, serialized_public_key=None, aes_key=None, aes_iv=None):

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

        # loading aes if applicable, otherwise generating a base session
        if aes_key is not None and aes_iv is not None:
            self.aes_cipher = load_cipher(aes_key, aes_iv)
        else:
            self.aes_cipher = generate_cipher_aes()

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

    def new_aes_session(self):
        self.aes_cipher = generate_cipher_aes()

    def load_aes_session(self, aes_key, aes_iv):
        self.aes_cipher = load_cipher(aes_key, aes_iv)

    def encrypt_aes(self, message, base64):
        ct = encrypt_aes(self.aes_cipher, message)

        if base64 == True:
            ct = encode(ct)

        return ct

    def decrypt_aes(self, ct, base64):

        if base64 == True:
            ct = decode(ct)

        try:
            message = decrypt_aes(self.aes_cipher, ct)
        except:
            message = None
        return message

    def serialize_aes(self, base64):
        
        if self.private_key is not None:
            serialized_aes = serialize_aes(self.aes_cipher, True, self.private_key)
        elif self.public_key is not None:
            serialized_aes = serialize_aes(self.aes_cipher, True, self.public_key)

        if base64 == True:
            serialized_aes = encode(serialized_aes)

        return serialized_aes

    def deserialize_aes(self, aes, base64):

        if base64 == True:
            aes = decode(aes)

        if self.private_key is not None:
            aes = deserialize_aes(aes, True, self.private_key)
        
        self.aes_cipher = aes

        return aes 