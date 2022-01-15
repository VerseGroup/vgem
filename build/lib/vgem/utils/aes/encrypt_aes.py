# crypto imports
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def encrypt_aes(cipher, message):
    message = message.encode('utf-8')
    encryptor = cipher.encryptor()
    ct = encryptor.update(message) + encryptor.finalize()
    return ct