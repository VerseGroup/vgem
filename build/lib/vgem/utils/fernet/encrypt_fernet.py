#crypto imports
from cryptography.fernet import Fernet

def encrypt_fernet(fernet, message):
    message = message.encode('utf-8')
    token = fernet.encrypt(message)
    return token