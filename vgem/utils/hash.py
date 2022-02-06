import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

def hash_(message):
    salt = os.urandom(16)
    kdf = Scrypt( 
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1)
    key = kdf.derive(message.encode('utf-8'))
    return {
        'salt': salt,
        'hash': key,
    }
    
def check_hash_(message, salt, hash):
    message = message.encode('utf-8')
    kdf = Scrypt( 
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1)
    return kdf.verify(message, hash)
    

