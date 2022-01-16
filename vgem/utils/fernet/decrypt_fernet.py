#crypto imports
from cryptography.fernet import Fernet

def decrypt_fernet(fernet, token):
    message = fernet.decrypt(token)
    message = message.decode('utf-8')
    return message