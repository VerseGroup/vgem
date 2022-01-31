from cryptography.hazmat.primitives import hashes
#from vgem.utils.base64ec import encode, decode

def hash_(message):
    message = message.encode('utf-8')
    digest = hashes.Hash(hashes.SHA256())
    digest.update(message)
    return digest.finalize()
    
def check_hash(message, existing_hash):
    return hash_(message) == existing_hash

