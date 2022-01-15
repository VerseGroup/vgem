# crypto imports
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def decrypt_aes(cipher, ct):
    decryptor = cipher.decryptor()
    decryptor.update(ct) + decryptor.finalize()
    ct = ct.decode('utf-8')
    return ct
